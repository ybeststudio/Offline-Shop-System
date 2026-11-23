#include "stdafx.h"
#undef false
#undef true
#include "../../common/tables.h"
#include "packet.h"
#include "item.h"
#include "char.h"
#include "item_manager.h"
#include "desc.h"
#include "char_manager.h"

#include "ikarus_shop.h"
#include "ikarus_shop_manager.h"

#ifdef ENABLE_IKASHOP_RENEWAL


namespace ikashop
{
	TItemTable* CShopItem::GetTable() const
	{
		return ITEM_MANAGER::instance().GetTable(m_info.vnum);
	}

	const TPriceInfo& CShopItem::GetPrice() const
	{
		return m_info.price;
	}

	LPITEM CShopItem::CreateItem() const
	{
		if(auto item = ITEM_MANAGER::instance().CreateItem(m_info.vnum, m_info.count, GetID()))
		{
			item->SetAttributes(m_info.aAttr);
			item->SetSockets(m_info.alSockets);
#ifdef ENABLE_CHANGELOOK_SYSTEM
			item->SetTransmutation(m_info.dwTransmutation);
#endif
			return item;
		}

		return nullptr;
	}

	const TShopItem& CShopItem::GetInfo() const
	{
		return m_info;
	}

	void CShopItem::SetInfo(const TShopItem& info)
	{
		m_info = info;
	}

	void CShopItem::SetPrice(const TPriceInfo& price)
	{
		m_info.price = price;
	}
	
	DWORD CShopItem::GetID() const
	{
		return m_info.id;
	}

	bool CShopItem::CanBuy(LPCHARACTER ch)
	{
		if(!ch)
			return false;

		if(m_info.price.yang > static_cast<long long>(ch->GetGold()))
			return false;
#ifdef ENABLE_CHEQUE_SYSTEM
		if(m_info.price.cheque > ch->GetCheque())
			return false;
#endif
		return true;
	}

	void CShopItem::SetCell(int pos)
	{
		m_info.pos = pos;
	}

	const CShop::SHOP_ITEM_MAP& CShop::GetItems() const
	{
		return m_items;
	}

	const CShop::OFFER_MAP& CShop::GetOffers() const
	{
		return m_offers;
	}

	const CShop::VECGUEST& CShop::GetGuests() const
	{
		return m_guests;
	}

	void CShop::SetDuration(DWORD duration)
	{
		m_duration=duration;
	}

	void CShop::DecreaseDuration()
	{
#ifdef EXTEND_IKASHOP_ULTIMATE
		if(m_decorationTime > 0)
			m_decorationTime--;
#endif

		m_duration--;
		_RefreshViews();
	}

	DWORD CShop::GetDuration() const
	{
		return m_duration;
	}

	void CShop::SetOwnerPID(DWORD ownerid)
	{
		m_pid = ownerid;
	}

	DWORD CShop::GetOwnerPID() const
	{
		return m_pid;
	}

	bool CShop::AddGuest(LPCHARACTER ch)
	{
		m_guests.emplace(ch->GetPlayerID());
		GetManager().SendShopOpenClientPacket(ch, this);
		return true;
	}

	bool CShop::RemoveGuest(LPCHARACTER ch)
	{
		return m_guests.erase(ch->GetPlayerID()) != 0;
	}

	void CShop::KickAllGuests()
	{
		auto guests{ GetGuests() };
		for (auto& guest : guests) 
		{
			if (auto chGuest = CHARACTER_MANAGER::instance().FindByPID(guest)) 
			{
				if (chGuest->GetIkarusShopGuest().get() == this) 
				{
					GetManager().SendShopExpiredGuesting(GetOwnerPID(), chGuest);
					chGuest->SetIkarusShopGuest(nullptr);
				}
			}
		}
	}

	bool CShop::AddItem(const TShopItem& item)
	{
		auto sitem = std::make_shared<CShopItem>();
		sitem->SetInfo(item);
		
		m_items[item.id] = sitem;
		
		if(auto table = sitem->GetTable()){
#ifdef EXTEND_IKASHOP_ULTIMATE
			const auto page = item.pos / (GRID_SIZE);
			const auto localPos = item.pos % GRID_SIZE;
			if(page >= 0 && page < PAGE_COUNT)
				m_grid[page].RegisterItem(localPos, table->bSize);
#else
			m_grid.RegisterItem(item.pos, table->bSize);
#endif
		}
		
		_RefreshViews();
		
		return true;
	}

	bool CShop::RemoveItem(DWORD itemid)
	{
		auto item = GetItem(itemid);
		if(!item)
			return false;

		m_items.erase(itemid);
		
		if(auto table = item->GetTable()){
#ifdef EXTEND_IKASHOP_ULTIMATE
			const auto page = item->GetInfo().pos / (GRID_SIZE);
			const auto localPos = item->GetInfo().pos % GRID_SIZE;
			if (page >= 0 && page < PAGE_COUNT)
				m_grid[page].UnregisterItem(localPos, table->bSize);
#else
			m_grid.UnregisterItem(item->GetInfo().pos, table->bSize);
#endif
		}
		
		TPacketGCNewIkarusShop pack{};
		pack.header = HEADER_GC_NEW_OFFLINESHOP;
		pack.size = sizeof(pack) + sizeof(TSubPacketGCShopRemoveItem);
		pack.subheader = SUBHEADER_GC_SHOP_REMOVE_ITEM_GUEST;

		TSubPacketGCShopRemoveItem subpack{};
		subpack.itemid = itemid;

		for (auto& guest : m_guests)
		{
			if (auto ch = CHARACTER_MANAGER::Instance().FindByPID(guest))
			{
				if (ch->GetDesc())
				{
					ch->GetDesc()->BufferedPacket(&pack, sizeof(pack));
					ch->GetDesc()->Packet(&subpack, sizeof(subpack));
				}
			}
		}

		pack.subheader = SUBHEADER_GC_SHOP_REMOVE_ITEM_OWNER;
		if(auto ch = FindOwnerCharacter())
		{
			if(ch->GetDesc())
			{
				ch->GetDesc()->BufferedPacket(&pack, sizeof(pack));
				ch->GetDesc()->Packet(&subpack, sizeof(subpack));
			}
		}
		
		return true;
	}

	bool CShop::ModifyItemPrice(DWORD itemid, const TPriceInfo& price)
	{
		auto shopItem = GetItem(itemid);
		if(!shopItem)
			return false;

		shopItem->SetPrice(price);
		
		TPacketGCNewIkarusShop pack{};
		pack.header = HEADER_GC_NEW_OFFLINESHOP;
		pack.subheader = SUBHEADER_GC_SHOP_EDIT_ITEM_GUEST;
		pack.size = sizeof(pack) + sizeof(TSubPacketGCShopEditItem);

		TSubPacketGCShopEditItem subpack{};
		subpack.itemid = itemid;
		subpack.price = price;

		for (auto& guest : m_guests)
		{
			if (auto ch = CHARACTER_MANAGER::Instance().FindByPID(guest))
			{
				if (ch->GetDesc())
				{
					ch->GetDesc()->BufferedPacket(&pack, sizeof(pack));
					ch->GetDesc()->Packet(&subpack, sizeof(subpack));
				}
			}
		}

		pack.subheader = SUBHEADER_GC_SHOP_EDIT_ITEM_OWNER;
		if (auto ch = FindOwnerCharacter())
		{
			if (ch->GetDesc())
			{
				ch->GetDesc()->BufferedPacket(&pack, sizeof(pack));
				ch->GetDesc()->Packet(&subpack, sizeof(subpack));
			}
		}

		return true;
	}

	bool CShop::BuyItem(DWORD itemid)
	{
		return RemoveItem(itemid);
	}

	CShop::ITEM_HANDLE CShop::GetItem(DWORD itemid)
	{
		auto it = m_items.find(itemid);
		return it != m_items.end() ? it->second : nullptr;
	}

	bool CShop::AddOffer(OFFER_HANDLE offer)
	{
		if(!m_items.contains(offer->itemid))
			return false;

		m_offers[offer->offerid] = offer;

		if (!offer->notified && !offer->accepted)
		{
			if (auto owner = FindOwnerCharacter())
			{
				if (owner->GetIkarusShop() && owner->IsLookingShopOwner())
				{
					NotifyOffers(owner);
					GetManager().SendShopOpenMyShopClientPacket(owner);
				}
			}
		}

		return true;
	}

	bool CShop::AcceptOffer(OFFER_HANDLE offer)
	{
		if(auto item = GetItem(offer->itemid))
		{
			item->SetPrice(offer->price);
			BuyItem(item->GetID());

			std::erase_if(m_offers, [&](auto& iter) { return iter.second->offerid == offer->offerid; });
			return true;
		}

		return false;
	}

	void CShop::_RefreshViews(LPCHARACTER ch)
	{
		for (auto& guest : m_guests)
			if (auto ch = CHARACTER_MANAGER::Instance().FindByPID(guest))
				GetManager().SendShopOpenClientPacket(ch, this);

		RefreshToOwner();
	}

	void CShop::Clear()
	{
		m_items.clear();
		m_offers.clear();
		m_guests.clear();
#ifdef EXTEND_IKASHOP_ULTIMATE
		for(auto& grid : m_grid)
			grid.Clear();
#else
		m_grid.Clear();
#endif
	}

	LPCHARACTER CShop::FindOwnerCharacter()
	{
		return CHARACTER_MANAGER::instance().FindByPID(GetOwnerPID());
	}

	void CShop::NotifyOffers(LPCHARACTER ch)
	{
		for (auto& [id, offer] : m_offers)
		{
			if (!offer->notified && !offer->accepted)
			{
				offer->notified = true;
				GetManager().SendShopOfferNotifiedDBPacket(offer->offerid, offer->ownerid);
			}
		}
	}

	void CShop::NotifyAcceptedOffers(LPCHARACTER ch)
	{
		for (auto& [id, offer] : m_offers)
		{
			if (!offer->notified && offer->accepted)
			{
				offer->notified = true;
				GetManager().SendShopOfferNotifiedDBPacket(offer->offerid, offer->ownerid);
			}
		}
	}

	void CShop::RemoveOffer(DWORD offerid)
	{
		std::erase_if(m_offers, [&](auto&& iter){ return offerid == iter.second->offerid; });
	}

	void CShop::_SendNotifyOffer(LPCHARACTER ch, const TOfferInfo& offer)
	{
	}

#ifdef EXTEND_IKASHOP_ULTIMATE
	void CShop::_RefreshGrid()
	{
		for (auto& grid : m_grid)
			grid.Clear();

		for (auto& [id, item] : m_items)
			if (auto table = item->GetTable())
				ReserveSpace(item->GetInfo().pos, table->bSize);

		for (int cell = GetLockIndex(); cell < GRID_SIZE * PAGE_COUNT; cell++)
			ReserveSpace(cell, 1);
	}
#endif

	const char* CShop::GetName() const
	{
		return m_name.c_str();
	}

	bool CShop::ReserveSpace(int cell, int size)
	{
#ifdef EXTEND_IKASHOP_ULTIMATE
		const auto page = cell / GRID_SIZE;
		const auto localPos = cell % GRID_SIZE;
		if(page < 0 || page >= PAGE_COUNT)
			return false;

		if (!m_grid[page].CheckSpace(localPos, size))
			return false;

		m_grid[page].RegisterItem(localPos, size);
#else
		if(!m_grid.CheckSpace(cell, size))
			return false;
		m_grid.RegisterItem(cell, size);
#endif
		return true;
	}

	int CShop::GetNewOffersCounter() const
	{
		return m_offers.size();
	}

#ifdef EXTEND_IKASHOP_ULTIMATE
	void CShop::MoveItem(DWORD itemid, int destCell)
	{
		if(auto item = GetItem(itemid))
		{
			if(auto table = item->GetTable())
			{
				const auto page = item->GetInfo().pos / (GRID_SIZE);
				const auto localPos = item->GetInfo().pos % GRID_SIZE;
				if (page >= 0 && page < PAGE_COUNT)
					m_grid[page].UnregisterItem(localPos, table->bSize);

				ReserveSpace(destCell, table->bSize);
			}

			item->SetCell(destCell);

			_RefreshViews();
		}
	}

	void CShop::ChangeDuration(DWORD duration)
	{
		SetDuration(duration);
		_RefreshViews();
	}


	void CShop::SetDecoration(int decoration)
	{
		m_decoration = decoration;
	}

	void CShop::SetDecorationDuration(int decoration_time)
	{
		m_decorationTime = decoration_time;
	}

	int CShop::GetDecoration() const
	{
		return m_decoration;
	}

	int CShop::GetDecorationTime() const
	{
		return m_decorationTime;
	}

	void CShop::SetLockIndex(int lockIndex)
	{
		m_lockIndex = lockIndex;
		_RefreshGrid();
	}

	int CShop::GetLockIndex() const
	{
		return m_lockIndex;
	}

	void CShop::ChangeLockIndex(int lockIndex)
	{
		if (GetLockIndex() < lockIndex)
			SetLockIndex(lockIndex);
		_RefreshViews();
	}
#endif

#ifdef ENABLE_IKASHOP_ENTITIES
	void CShop::SetEntity(ENTITY_HANDLE handle)
	{
		m_entity = handle;
	}

	CShop::ENTITY_HANDLE CShop::GetEntity() const
	{
		return m_entity;
	}

	void CShop::SetSpawn(const TShopSpawn& spawn)
	{
		m_spawn = spawn;
	}

	const TShopSpawn& CShop::GetSpawn() const
	{
		return m_spawn;
	}
#endif

	void CShop::SetName(const SHOPNAME& name)
	{
		m_name = name;
	}

	void CShop::RefreshToOwner()
	{
		if(auto ch = FindOwnerCharacter())
			if(ch->IsLookingShopOwner())
				GetManager().SendShopOpenMyShopClientPacket(ch);
	}

	void CAuction::SetInfo(const TAuctionInfo& auction)
	{
		m_info = auction;
	}

	void CAuction::SetOffers(const std::vector<TAuctionOfferInfo>& vec)
	{
		m_offers.clear();
		m_offers.reserve(vec.size());

		for(auto& offer : vec)
			AddOffer(offer, false);

		CheckBestOffer();
	}

	bool CAuction::AddOffer(const TAuctionOfferInfo& offer, bool check)
	{
		m_offers.emplace_back(std::make_shared<TAuctionOfferInfo>(offer));
		if(check){
			CheckBestOffer();
			RefreshGuestView();
		}
		return true;
	}

	bool CAuction::AddGuest(LPCHARACTER ch)
	{
		const auto& pid = ch->GetPlayerID();
		if (std::find(m_guests.begin(), m_guests.end(), pid) != m_guests.end())
			return false;

		m_guests.push_back(ch->GetPlayerID());
		GetManager().SendAuctionOpenAuctionClientPacket(ch, *this);
		return true;
	}

	bool CAuction::RemoveGuest(LPCHARACTER ch)
	{
		return std::erase(m_guests, ch->GetPlayerID()) != 0;
	}

	void CAuction::IncreaseDuration()
	{
		m_info.duration++;
	}

	void CAuction::DecreaseDuration()
	{
		if(m_info.duration != 0)
			m_info.duration--;
	}

	const TAuctionInfo& CAuction::GetInfo() const
	{
		return m_info;
	}

	const CAuction::AUCTION_OFFERVEC& CAuction::GetOffers() const
	{
		return m_offers;
	}

	CAuction::AUCTION_OFFER_HANDLE CAuction::GetBestOffer() const
	{
		return m_bestOffer;
	}

	void CAuction::RefreshToOwner(LPCHARACTER ch)
	{
		if(auto owner = (ch ? ch : CHARACTER_MANAGER::instance().FindByPID(m_info.owner)))
			if(owner->IsLookingAuctionOwner())
				GetManager().SendAuctionOpenAuctionClientPacket(owner, *this);
	}

	int CAuction::GetNewOffersCounter() const
	{
		return std::count_if(m_offers.begin(), m_offers.end(), [](auto&& offer) { return offer->seenflag == false; });
	}

#ifdef ENABLE_IKASHOP_ENTITIES
	#ifdef EXTEND_IKASHOP_ULTIMATE
	void CAuction::SetEntity(ENTITY_HANDLE entity)
	{
		m_entity = entity;
	}

	CAuction::ENTITY_HANDLE CAuction::GetEntity()
	{
		return m_entity;
	}

	const TShopSpawn& CAuction::GetSpawn() const
	{
		return m_info.spawn;
	}
	#endif
#endif

	const CAuction::GUESTVEC& CAuction::GetGuests() const
	{
		return m_guests;
	}

	const DWORD CAuction::GetBestBuyer() const
	{
		return m_bestOffer ? m_bestOffer->buyerid : 0;
	}
	
	void CAuction::RefreshGuestView()
	{
		for(auto& guest : m_guests)
			if(auto ch = CHARACTER_MANAGER::instance().FindByPID(guest))
				GetManager().SendAuctionOpenAuctionClientPacket(ch, *this);

		RefreshToOwner();
	}

	bool CAuction::CheckBestOffer()
	{
		auto iter = std::max_element(m_offers.begin(), m_offers.end(), [](auto&& first, auto&& second) {
			return first->price.GetTotalYangAmount() < second->price.GetTotalYangAmount(); });
		m_bestOffer = iter != m_offers.end() ? *iter : nullptr;
		return bool(m_bestOffer);
	}

#ifdef ENABLE_IKASHOP_ENTITIES
	ShopEntity::ShopEntity()
	{
		CEntity::Initialize(ENTITY_NEWSHOPS);
	}

	void ShopEntity::EncodeInsertPacket(LPENTITY entity)
	{
		if(entity->GetType() != ENTITY_CHARACTER)
			return;

		auto ch = static_cast<LPCHARACTER>(entity);
		if(!ch->IsPC())
			return;

		if(GetShop() && GetShop()->GetDuration() == 0)
			return;

		GetManager().EncodeInsertShopEntity(*this, ch);
	}

	void ShopEntity::EncodeRemovePacket(LPENTITY entity)
	{
		if (entity->GetType() != ENTITY_CHARACTER)
			return;

		auto ch = static_cast<LPCHARACTER>(entity);
		if (!ch->IsPC())
			return;

		GetManager().EncodeRemoveShopEntity(*this, ch);
	}

	const char* ShopEntity::GetShopName() const
	{
		return m_name.c_str();
	}

	void ShopEntity::SetShopName(const char* name)
	{
		m_name = name;
	}

	int ShopEntity::GetShopType() const
	{
		return m_type;
	}

	void ShopEntity::SetShopType(int iType)
	{
		m_type = iType;
	}

	void ShopEntity::SetShop(SHOP_HANDLE shop)
	{
		m_shop = shop;
	}

#ifdef EXTEND_IKASHOP_ULTIMATE
	void ShopEntity::SetAuction(AUCTION_HANDLE auction)
	{
		m_auction = auction;
	}

	ShopEntity::AUCTION_HANDLE ShopEntity::GetAuction()
	{
		return m_auction;
	}
#endif
#endif
}



#endif







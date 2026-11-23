// void CClientManager::QUERY_BOOT(CPeer* peer, TPacketGDBoot * p) icinde:
// Ara:


	peer->EncodeWORD(0xffff);

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
	SendIkarusShopTable(peer);
#endif


// void CClientManager::QUERY_ITEM_SAVE(CPeer * pkPeer, const char * c_pData) icinde:
// Ara:
	TPlayerItem * p = (TPlayerItem *) c_pData;

	if (p->window == SAFEBOX || p->window == MALL

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
		|| p->window == IKASHOP_OFFLINESHOP || p->window == IKASHOP_SAFEBOX || p->window == IKASHOP_AUCTION
#endif


// void CClientManager::ProcessPackets(CPeer * peer) icinde:
// Ara:
			case HEADER_GD_REQUEST_CHANNELSTATUS:
				RequestChannelStatus(peer, dwHandle);
				break;

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
			case HEADER_GD_NEW_OFFLINESHOP:
				RecvIkarusShopPacket(peer, data);
				break;
#endif


// int CClientManager::AnalyzeQueryResult(SQLMsg * msg) icinde:
// Ara:
			RESULT_PRICELIST_LOAD_FOR_UPDATE(msg);
			break;
	}

	if (!peer)
	{

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
		switch (qi->iType)
		{
		case QID_OFFLINESHOP_ADD_ITEM:
		case QID_OFFLINESHOP_EDIT_ITEM:
		case QID_OFFLINESHOP_DELETE_SHOP:
		case QID_OFFLINESHOP_DELETE_SHOP_ITEM:
		case QID_OFFLINESHOP_REMOVE_ITEM:
		case QID_OFFLINESHOP_UPDATE_SOLD_ITEM:
		case QID_OFFLINESHOP_CREATE_SHOP:
		case QID_OFFLINESHOP_SHOP_CHANGE_NAME:
		case QID_OFFLINESHOP_SHOP_UPDATE_DURATION:
		case QID_OFFLINESHOP_SAFEBOX_DELETE_ITEM:
		case QID_OFFLINESHOP_SAFEBOX_ADD_ITEM:
		case QID_OFFLINESHOP_SAFEBOX_UPDATE_VALUTES:
		case QID_OFFLINESHOP_SAFEBOX_INSERT_VALUTES:
		case QID_OFFLINESHOP_SAFEBOX_UPDATE_VALUTES_ADDING:
		case QID_OFFLINESHOP_OFFER_ADD:
		case QID_OFFLINESHOP_OFFER_UPDATE_NOTIFIED:
		case QID_OFFLINESHOP_OFFER_UPDATE_ACCEPTED:
		case QID_OFFLINESHOP_OFFER_DELETE_BY_SHOP:
		case QID_OFFLINESHOP_AUCTION_INSERT:
		case QID_OFFLINESHOP_AUCTION_INSERT_OFFER:
		case QID_OFFLINESHOP_AUCTION_DELETE:
		case QID_OFFLINESHOP_AUCTION_DELETE_OFFERS:
		case QID_OFFLINESHOP_AUCTION_UPDATE_DURATION:
			IkarusShopResultQuery(peer, msg, qi);
			break;

		default: break;
		}
#endif


// int CClientManager::AnalyzeQueryResult(SQLMsg * msg) icinde:
// Ara:
		case QID_ITEMPRICE_LOAD:
			RESULT_PRICELIST_LOAD(peer, msg);
			break;

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
		case QID_OFFLINESHOP_ADD_ITEM:
		case QID_OFFLINESHOP_EDIT_ITEM:
		case QID_OFFLINESHOP_DELETE_SHOP:
		case QID_OFFLINESHOP_DELETE_SHOP_ITEM:
		case QID_OFFLINESHOP_CREATE_SHOP:
		case QID_OFFLINESHOP_SHOP_CHANGE_NAME:
		case QID_OFFLINESHOP_SAFEBOX_DELETE_ITEM:
		case QID_OFFLINESHOP_SAFEBOX_ADD_ITEM:
		case QID_OFFLINESHOP_REMOVE_ITEM:
		case QID_OFFLINESHOP_SAFEBOX_UPDATE_VALUTES:
		case QID_OFFLINESHOP_SAFEBOX_INSERT_VALUTES:
		case QID_OFFLINESHOP_SAFEBOX_UPDATE_VALUTES_ADDING:
		case QID_OFFLINESHOP_OFFER_ADD:
		case QID_OFFLINESHOP_OFFER_UPDATE_NOTIFIED:
		case QID_OFFLINESHOP_OFFER_UPDATE_ACCEPTED:
		case QID_OFFLINESHOP_OFFER_DELETE_BY_SHOP:
		case QID_OFFLINESHOP_AUCTION_INSERT:
		case QID_OFFLINESHOP_AUCTION_INSERT_OFFER:
		case QID_OFFLINESHOP_AUCTION_DELETE:
		case QID_OFFLINESHOP_AUCTION_DELETE_OFFERS:
		case QID_OFFLINESHOP_AUCTION_UPDATE_DURATION:
			IkarusShopResultQuery(peer, msg, qi);
			break;
#endif


// int CClientManager::Process() icinde:
// Ara:
		{
			ItemAwardManager::instance().RequestLoad();
		}

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
		if ((thecore_heart->pulse % (thecore_heart->passes_per_sec * 60)) == thecore_heart->passes_per_sec*30)
			IkarusShopDurationProcess();
#endif

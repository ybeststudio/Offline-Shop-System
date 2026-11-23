// Ara:
{
	GuildShop_Command(ch, argument);
}
#endif

// Altina ekle:
#ifdef ENABLE_IKASHOP_SEARCH_RENEWAL
#include "ikarus_shop_manager.h"
#include "db.h"
ACMD(do_anka_open_shop)
{
	if (!ch || !ch->IsPC() || !ch->GetDesc())
		return;

	char arg1[CHARACTER_NAME_MAX_LEN + 1];
	one_argument(argument, arg1, sizeof(arg1));
	if (!*arg1)
		return;

	DWORD pid = 0;
	if (LPCHARACTER target = CHARACTER_MANAGER::instance().FindPC(arg1))
		pid = target->GetPlayerID();
	else
	{
		char szName[CHARACTER_NAME_MAX_LEN * 2 + 1];
		DBManager::instance().EscapeString(szName, sizeof(szName), arg1, strlen(arg1));
		std::unique_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT id FROM player WHERE name = '%s' LIMIT 1", szName));
		if (pMsg && pMsg->Get() && pMsg->Get()->uiNumRows > 0)
		{
			MYSQL_ROW row = mysql_fetch_row(pMsg->Get()->pSQLResult);
			if (row && row[0])
				str_to_number(pid, row[0]);
		}
	}

	if (!pid || !ikashop::GetManager().GetShopByOwnerID(pid))
	{
		ch->ChatPacket(CHAT_TYPE_COMMAND, "AnkaOpenShopResult 0");
		return;
	}

	ikashop::GetManager().RecvShopOpenClientPacket(ch, pid);
}
#endif

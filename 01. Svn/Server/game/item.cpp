// LPITEM CItem::RemoveFromCharacter() icinde:
// Ara:
	else
	{
		if (GetWindow() != SAFEBOX && GetWindow() != MALL

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
			&& GetWindow() != IKASHOP_OFFLINESHOP
			&& GetWindow() != IKASHOP_AUCTION
			&& GetWindow() != IKASHOP_SAFEBOX
#endif

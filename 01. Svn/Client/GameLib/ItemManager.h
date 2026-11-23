// Ara:
		bool LoadAuraScale(const char *c_szFileName);
#endif
		CItemData *MakeItemData(DWORD dwIndex);

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
		void			GetItemsNameMap(std::map<DWORD, std::string>& inMap);
#endif

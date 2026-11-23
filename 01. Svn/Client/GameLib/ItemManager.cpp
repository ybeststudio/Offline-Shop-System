// Ara:
	rstTemp = c_rstSrc.substr(uLeftCut, uRightCut-uLeftCut);
	return rstTemp;
}

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
void CItemManager::GetItemsNameMap(std::map<DWORD, std::string>& inMap)
{
	inMap.clear();

	for(auto& it : m_ItemMap)
		inMap.insert(std::make_pair(it.first, it.second->GetName())); 
}
#endif

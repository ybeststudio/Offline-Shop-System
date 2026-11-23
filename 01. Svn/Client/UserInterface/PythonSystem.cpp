// void CPythonSystem::SetDefaultConfig() icinde:
// Ara:
	m_Config.bViewChat = true;
	m_Config.bAlwaysShowName = DEFAULT_VALUE_ALWAYS_SHOW_NAME;
	m_Config.bShowDamage = true;

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
#ifdef EXTEND_IKASHOP_PRO
	m_Config.shopRangeView = 5000.0f;
#endif
#endif


// bool CPythonSystem::LoadConfig() icinde:
// Ara:
			m_Config.bShowDamage = atoi(value) == 1 ? true : false;
		else if (!stricmp(command, "SHOW_SALESTEXT"))
			m_Config.bShowSalesText = atoi(value) == 1 ? true : false;

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
#ifdef EXTEND_IKASHOP_PRO
		else if (!stricmp(command, "SHOP_RANGE_VIEW"))
			m_Config.shopRangeView = std::stof(value);
#endif
#endif


// bool CPythonSystem::SaveConfig() icinde:
// Ara:
		fprintf(fp, "SHOW_DAMAGE			%d\n", m_Config.bShowDamage);
	if (m_Config.bShowSalesText == 0)
		fprintf(fp, "SHOW_SALESTEXT			%d\n", m_Config.bShowSalesText);

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
#ifdef EXTEND_IKASHOP_PRO
	fprintf(fp, "SHOP_RANGE_VIEW		%f\n", m_Config.shopRangeView);
#endif
#endif

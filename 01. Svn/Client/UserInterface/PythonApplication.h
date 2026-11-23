// Ara:
constexpr float c_fDefaultSpecularPower = 0.5f;
constexpr float c_fMinSpecularPower = 0.0f;
constexpr float c_fMaxSpecularPower = 1.0f;

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
#include "PythonIkarusShop.h"
#endif


// Ara:
		CPythonMiniMap m_pyMiniMap;
		CPythonEventManager m_pyEventManager;
		CPythonBackground m_pyBackground;

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
		CPythonIkarusShop			m_pyOfflineshop;
#endif

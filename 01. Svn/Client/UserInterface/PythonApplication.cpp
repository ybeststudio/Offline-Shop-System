// void CPythonApplication::RenderGame() icinde:
// Ara:
	STATEMANAGER.SetVertexShader(nullptr);
	STATEMANAGER.SetPixelShader(nullptr);
	m_kEftMgr.Render();

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
		m_pyOfflineshop.RenderEntities();
#endif


// void CPythonApplication::UpdateGame() icinde:
// Ara:
	uint32_t t5 = ELTimer_GetMSec();
	m_GameEventManager.SetCenterPosition(kPPosMainActor.x, kPPosMainActor.y, kPPosMainActor.z);
	m_GameEventManager.Update();

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
	m_pyOfflineshop.UpdateEntities();
#endif


// void CPythonApplication::Destroy() icinde:
// Ara:
#endif

void CPythonApplication::Destroy()
{

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
	CPythonIkarusShop::instance().DeleteEntities();
#endif

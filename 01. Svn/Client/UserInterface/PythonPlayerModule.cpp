// Ara:
	return Py_BuildValue("b", CPythonPlayer::Instance().CanAttachToCombItemSlot(bSlot, TItemPos(bWindowType, wCell)));
}
#endif

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
#ifdef EXTEND_IKASHOP_PRO
PyObject* playerRefreshInventory(PyObject* poSelf, PyObject* poArgs)
{
	CPythonPlayer::Instance().RefreshInventory();

	return Py_BuildNone();
}
#endif
#endif


// void initPlayer() icinde:
// Ara:
		{ "SetItemCount", playerSetItemCount, METH_VARARGS },

		{ "GetItemLink", playerGetItemLink, METH_VARARGS },

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
#ifdef EXTEND_IKASHOP_PRO
		{ "RefreshInventory",			playerRefreshInventory,				METH_VARARGS },
#endif
#endif


// void initPlayer() icinde:
// Ara:
	PyModule_AddIntConstant(poModule, "SAFEBOX",							SAFEBOX);
	PyModule_AddIntConstant(poModule, "MALL",								MALL);
	PyModule_AddIntConstant(poModule, "DRAGON_SOUL_INVENTORY",				DRAGON_SOUL_INVENTORY);

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
#ifdef EXTEND_IKASHOP_ULTIMATE
	PyModule_AddIntConstant(poModule, "SLOT_TYPE_OFFLINESHOP",				SLOT_TYPE_OFFLINESHOP);
#ifdef ENABLE_WARDROBE_ITEM_TRANSFER
	PyModule_AddIntConstant(poModule, "SLOT_TYPE_WARDROBE",				SLOT_TYPE_WARDROBE);
#endif
	PyModule_AddIntConstant(poModule, "IKASHOP_OFFLINESHOP",				IKASHOP_OFFLINESHOP);
	PyModule_AddIntConstant(poModule, "IKASHOP_SAFEBOX",					IKASHOP_SAFEBOX);
	PyModule_AddIntConstant(poModule, "IKASHOP_AUCTION",					IKASHOP_AUCTION);
#endif
#endif

// Ara:
    if (PyTuple_Size(args) > 1 && !PyTuple_GetFloat(args, 1, &fallback)) return Py_BuildException();
    return Py_BuildValue("f", CPythonSystem::Instance().GetAdvancedOption(key, fallback));
}

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
#ifdef EXTEND_IKASHOP_PRO
PyObject* systemGetShopRangeView(PyObject* poSelf, PyObject* poArgs)
{
	return PyFloat_FromDouble(CPythonSystem::instance().GetShopRangeView());
}

PyObject* systemSetShopRangeView(PyObject* poSelf, PyObject* poArgs)
{
	float view = 0.0f;
	if(!PyTuple_GetFloat(poArgs, 0, &view))
		return Py_BadArgument();

	CPythonSystem::instance().SetShopRangeView(view);
	return Py_BuildNone();
}
#endif
#endif


// void initsystem() icinde:
// Ara:
		{ "IsShowSalesText",			systemIsShowSalesText,			METH_VARARGS },

		{ "GetShadowLevel",				systemGetShadowLevel,			METH_VARARGS },

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
#ifdef EXTEND_IKASHOP_PRO
		{"GetShopRangeView",			systemGetShopRangeView,			METH_VARARGS },
		{"SetShopRangeView",			systemSetShopRangeView,			METH_VARARGS },
#endif
#endif

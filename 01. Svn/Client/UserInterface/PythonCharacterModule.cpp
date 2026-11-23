// void initchr() icinde:
// Ara:
	PyModule_AddIntConstant(poModule, "NEW_AFFECT_DRAGON_SOUL_DECK1", CInstanceBase::NEW_AFFECT_DRAGON_SOUL_DECK1);
	PyModule_AddIntConstant(poModule, "NEW_AFFECT_DRAGON_SOUL_DECK2", CInstanceBase::NEW_AFFECT_DRAGON_SOUL_DECK2);

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
#ifdef EXTEND_IKASHOP_ULTIMATE
	PyModule_AddIntConstant(poModule, "NEW_AFFECT_SEARCH_SHOP_PREMIUM", CInstanceBase::NEW_AFFECT_SEARCH_SHOP_PREMIUM);
#endif
#endif

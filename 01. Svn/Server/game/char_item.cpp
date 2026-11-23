// Ara:
#include "utils.h"
#include "config.h"
#include "char.h"

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
#ifdef EXTEND_IKASHOP_ULTIMATE
#include "ikarus_shop_manager.h"
#endif
#endif


// bool CHARACTER::UseItemEx(LPITEM item, TItemPos DestCell) icinde:
// Ara:
								ForgetMyAttacker();
								item->SetCount(item->GetCount()-1);
								break;

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
#ifdef EXTEND_IKASHOP_ULTIMATE
							case 51998:
								if (ikashop::GetManager().UsePrivateShopKey(this, item))
									item->SetCount(item->GetCount() - 1);
								break;

							case 51999:
								if (ikashop::GetManager().UseSearchShopPremium(this, item))
									item->SetCount(item->GetCount() - 1);
								break;
#endif
#endif

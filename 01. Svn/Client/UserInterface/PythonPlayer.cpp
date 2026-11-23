// Ara:
			if (pOtherItemData->GetSubType() != bItemSubType)
				return false;
		}
	}

	return true;
}
#endif

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
#ifdef EXTEND_IKASHOP_PRO
void CPythonPlayer::RefreshInventory()
{
	PyCallClassMemberFunc(m_ppyGameWindow, "RefreshInventory", Py_BuildValue("()"));
}
#endif
#endif

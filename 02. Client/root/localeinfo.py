# def ShopSecondsToDHM(time) icinde:
# Ara:
def ShopSecondsToDHM(time):
	if time < 60:
		if IsARABIC():

# Altina ekle / satiri bu hale getir:
			return "%.2f%s" % (time, IKASHOP_SECOND)


# def ShopSecondsToDHM(time) icinde:
# Ara:
def ShopSecondsToDHM(time):
	if time < 60:
		if IsARABIC():
		else:

# Altina ekle / satiri bu hale getir:
			return "0" + IKASHOP_MINUTE


# def ShopSecondsToDHM(time) icinde:
# Ara:
	day = int(int((time / 60) / 60) / 24)

	text = ""

	if day > 0:

# Altina ekle / satiri bu hale getir:
		text += str(day) + IKASHOP_DAY


# def ShopSecondsToDHM(time) icinde:
# Ara:
	text = ""

	if day > 0:
		text += " "

	if hour > 0:

# Altina ekle / satiri bu hale getir:
		text += str(hour) + IKASHOP_HOUR


# def ShopSecondsToDHM(time) icinde:
# Ara:
		text += " "

	if hour > 0:
		text += " "

	if minute > 0:

# Altina ekle / satiri bu hale getir:
		text += str(minute) + IKASHOP_MINUTE


# Ara:
LOCALE_FILE_NAME = "%s/locale_game.txt" % app.GetLocalePath()
LoadLocaleFile(LOCALE_FILE_NAME, LOCALE_TEXT_DICT)

# Altina ekle:
if app.ENABLE_IKASHOP_RENEWAL:
	LoadLocaleFile("locale/common/locale_game_ikashop.txt", LOCALE_TEXT_DICT)

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
button_anime = KeyboardButton("/ANIME")
button_quiz = KeyboardButton("/quiz")
button_survey = KeyboardButton("/talk")
button_jokes = KeyboardButton("/jokes")
button_moderation = KeyboardButton("/moderator")
button_location = KeyboardButton("/Share location", request_location=True)
button_info = KeyboardButton("/Share info", request_contact=True)
keyboard_stat = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)


keyboard_stat.add(button_quiz, button_survey, button_jokes, button_moderation, button_location, button_info, button_anime)

import asyncio
from aiogram import Bot, Dispatcher

from .config_data.config import load_config
from .handlers import get_routers


# Подключаем логирование


async def main() -> None:
    dp: Dispatcher = Dispatcher()

    # Активация телеграмм бота
    bot_config = load_config()

    bot: Bot = Bot(
        token=bot_config.tg_bot.token,
        )

    dp.include_routers(*get_routers())

    # Запускаем polling
    try:
        await bot.delete_webhook(drop_pending_updates=True)

        await dp.start_polling(
                bot,
            )
    except KeyboardInterrupt:
        print('Bot stopped by user')
    except SystemExit:
        print('Bot stopped by system exit')
    except Exception as e:
        print(e)


asyncio.run(main())

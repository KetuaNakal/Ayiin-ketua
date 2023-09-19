# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

import os


from AyiinXd import Ayiin
from AyiinXd.ayiin import ayiin_cmd, eor

from . import var

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


@ayiin_cmd(pattern="curi(?: |$)(.*)")
async def mencuri(yins):
    xx = await eor(yins, "Memprosess...")
    url = yins.pattern_match.group(1)
    if url.startswith('https'):
        msg_id = int(url.split("/")[-1])
        if "t.me/c/" in url:
            chat = int("-100" + str(url.split("/")[-2]))
        else:
            chat = str(url.split("/")[-2])
        try:
            target = await Ayiin.get_messages(
                chat,
                ids=msg_id,
            )
            pesan=tks
            for i in target:
                tks=await i.message
                file = await Ayiin.download_media(
                    target,
                    var.TEMP_DOWNLOAD_DIRECTORY,
                )
                await Ayiin.send_file(
                    yins.chat_id,
                    file,
                    caption=f"{pesan}\n[ SUCCESS ] - Colong Konten By Ayiin-Userbot.",
                )
            await xx.delete()
            os.remove(file)
        except Exception as e:  # pylint:disable=C0103,W0703
            await xx.edit(str(e))
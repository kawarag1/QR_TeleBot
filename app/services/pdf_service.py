from tempfile import gettempdir
from telebot import async_telebot
from telebot import types
# from docx2pdf import convert
import img2pdf
import asyncio
import subprocess
import os

class PDFService():
    
    @staticmethod
    async def convert_docx_to_pdf(bot: async_telebot, message: types.Message):
        try:
            file_info = await bot.get_file(message.document.file_id)
            downloaded_file = await bot.download_file(file_info.file_path)

            temp_dir = gettempdir()
            docx_path = os.path.join(temp_dir, message.document.file_name)
            pdf_path = os.path.join(temp_dir, os.path.splitext(message.document.file_name)[0] + ".pdf")

            with open(docx_path, 'wb') as file:
                file.write(downloaded_file)
            
            # convert(docx_path, pdf_path)
            process = await asyncio.create_subprocess_exec(
                'libreoffice',
                '--headless',
                '--convert-to', 'pdf:writer_pdf_Export',
                '--outdir', temp_dir,
                docx_path,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            await process.wait()
            
            if process.returncode != 0:
                raise Exception("Ошибка конвертации LibreOffice")

            with open(pdf_path, 'rb') as pdf_file:
                await bot.send_document(
                    chat_id = message.chat.id,
                    document = pdf_file,
                    caption = f"✅ Ваш файл `{message.document.file_name}` конвертирован в PDF!",
                    reply_to_message_id=message.message_id,
                    parse_mode="Markdown"
                )
            os.remove(docx_path)
            os.remove(pdf_path)

        except Exception as e:
            await bot.reply_to(message, f"❌ Ошибка при конвертации: {str(e)}")
        
    @staticmethod
    async def convert_image_to_pdf(bot: async_telebot, message: types.Message):
        try:
            file_id = message.photo[-1].file_id
            file_info = await bot.get_file(file_id)
            downloaded_file = await bot.download_file(file_info.file_path)

            temp_dir = gettempdir()
            img_path = os.path.join(temp_dir, f"temp_{file_id}.jpg")
            pdf_path = os.path.join(temp_dir, f"converted_{file_id}.pdf")

            with open(img_path, 'wb') as f:
                f.write(downloaded_file)

            with open(pdf_path, "wb") as pdf_file:
                pdf_file.write(img2pdf.convert(img_path))

            with open(pdf_path, 'rb') as pdf_file:
                await bot.send_document(
                    chat_id=message.chat.id,
                    document=pdf_file,
                    caption="✅ Изображение конвертировано в PDF!",
                    reply_to_message_id=message.message_id
                )

            os.remove(img_path)
            os.remove(pdf_path)

        except Exception as e:
            await bot.reply_to(message, f"❌ Ошибка при конвертации: {str(e)}")
        
from app.services.pdf_service import PDFService

from app.bot.bot_instance import bot



@bot.message_handler(content_types = ['document', 'photo'])
async def handle_files(message):
    try:
        if message.document:
            if not message.document.file_name.endswith('.docx'):
                await bot.reply_to(message, "❌ Пожалуйста, отправьте файл в формате `.docx`!")
                return
            
            await PDFService.convert_docx_to_pdf(bot, message)
            
        elif message.photo:
            await PDFService.convert_image_to_pdf(bot, message)
    
    except Exception as e:
        await bot.reply_to(message, f"❌ Ошибка при конвертации: {str(e)}")


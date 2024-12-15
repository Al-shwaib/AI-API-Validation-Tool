# AI API Validation Tool

<div dir="ltr">

## Project Description
A versatile program that validates and interacts with multiple AI APIs including OpenAI's ChatGPT and Google's Gemini. It allows users to send prompts and receive responses from their chosen AI model, with detailed insights into the interaction.

## Features
1. **Multiple AI API Support**:
   - ChatGPT (OpenAI) API integration
   - Gemini (Google) API integration
   - Extensible structure for adding more AI services

2. **API Key Validation**:
   - Validates API keys before making actual requests
   - Provides immediate feedback on API key validity
   - Secure handling of API keys (runtime input only)

3. **Model Selection**:
   - For ChatGPT: Supports both GPT-4 and GPT-3.5 models
   - For Gemini: Uses the latest Gemini Pro model

4. **Robust Error Handling**:
   - Comprehensive error checking for API responses
   - Clear error messages for troubleshooting
   - Timeout protection for API requests

5. **Response Analysis**:
   - Formatted JSON response display
   - Model-specific response parsing
   - Usage statistics (for supported APIs)

6. **User-Friendly Interface**:
   - Simple menu for AI service selection
   - Clear prompts for user input
   - Organized output display

7. **Code Structure**:
   - Modular design with separate functions for each API
   - Type hints for better code clarity
   - Comprehensive error handling
   - Clean and maintainable codebase

## Requirements
- Python 3.6 or higher
- `requests` library
- API keys for the services you want to use:
  - OpenAI API key for ChatGPT
  - Google API key for Gemini

## Setup and Running Instructions
1. Install the required library:
```bash
pip install requests
```

2. Run the program:
```bash
python API_validation.py
```

3. Follow the prompts:
   - Choose your AI service (ChatGPT or Gemini)
   - Enter your API key when prompted
   - Type your prompt/question
   - View the response and any additional information

## Response Format
### ChatGPT
- Full JSON response
- Main response text
- Usage details (tokens used)
- Model information

### Gemini
- Full JSON response
- Main response text
- Additional response details when available

## Error Handling
The program handles various error cases:
- Invalid API keys
- Network connection issues
- API timeout errors
- Invalid response formats
- Service-specific errors

## Security Notes
- API keys are never stored in the code
- Keys are requested at runtime
- All API requests use secure HTTPS
- Timeout limits prevent hanging requests

</div>

---

<div dir="rtl">

# أداة التحقق من واجهات برمجة تطبيقات الذكاء الاصطناعي

## وصف المشروع
برنامج متعدد الاستخدامات يتحقق من صحة ويتفاعل مع العديد من واجهات برمجة تطبيقات الذكاء الاصطناعي بما في ذلك ChatGPT من OpenAI و Gemini من Google. يتيح للمستخدمين إرسال الاستفسارات وتلقي الردود من نموذج الذكاء الاصطناعي الذي يختارونه، مع رؤى تفصيلية حول التفاعل.

## الميزات
1. **دعم واجهات برمجة تطبيقات ذكاء اصطناعي متعددة**:
   - تكامل مع واجهة برمجة تطبيقات ChatGPT (OpenAI)
   - تكامل مع واجهة برمجة تطبيقات Gemini (Google)
   - هيكل قابل للتوسيع لإضافة المزيد من خدمات الذكاء الاصطناعي

2. **التحقق من صحة مفتاح API**:
   - يتحقق من صحة مفاتيح API قبل إجراء الطلبات الفعلية
   - يوفر تغذية راجعة فورية عن صحة مفتاح API
   - معالجة آمنة لمفاتيح API (إدخال وقت التشغيل فقط)

3. **اختيار النموذج**:
   - لـ ChatGPT: يدعم نماذج GPT-4 و GPT-3.5
   - لـ Gemini: يستخدم أحدث نموذج Gemini Pro

4. **معالجة قوية للأخطاء**:
   - فحص شامل لاستجابات API
   - رسائل خطأ واضحة لاستكشاف الأخطاء وإصلاحها
   - حماية من انتهاء المهلة لطلبات API

5. **تحليل الاستجابة**:
   - عرض استجابة JSON منسقة
   - تحليل الاستجابة حسب النموذج
   - إحصائيات الاستخدام (للواجهات المدعومة)

6. **سهل الاستخدام**:
   - قائمة بسيطة لاختيار خدمة الذكاء الاصطناعي
   - مطالبات واضحة لإدخال المستخدم
   - عرض منظم للمخرجات

7. **هيكل الكود**:
   - تصميم نمطي مع وظائف منفصلة لكل API
   - تلميحات النوع لوضوح أفضل للكود
   - معالجة شاملة للأخطاء
   - قاعدة كود نظيفة وقابلة للصيانة

## المتطلبات
- Python 3.6 أو أعلى
- مكتبة `requests`
- مفاتيح API للخدمات التي تريد استخدامها:
  - مفتاح OpenAI API لـ ChatGPT
  - مفتاح Google API لـ Gemini

## التثبيت والتشغيل
1. تثبيت المكتبة المطلوبة:
```bash
pip install requests
```

2. تشغيل البرنامج:
```bash
python API_validation.py
```

3. اتبع التعليمات:
   - اختر خدمة الذكاء الاصطناعي (ChatGPT أو Gemini)
   - أدخل مفتاح API عند الطلب
   - اكتب استفسارك/سؤالك
   - عرض الاستجابة والمعلومات الإضافية

## تنسيق الاستجابة
### ChatGPT
- استجابة JSON كاملة
- نص الاستجابة الرئيسي
- تفاصيل الاستخدام (الرموز المستخدمة)
- معلومات النموذج

### Gemini
- استجابة JSON كاملة
- نص الاستجابة الرئيسي
- تفاصيل الاستجابة الإضافية عند توفرها

## معالجة الأخطاء
يتعامل البرنامج مع حالات الخطأ المختلفة:
- مفاتيح API غير صالحة
- مشاكل الاتصال بالشبكة
- أخطاء انتهاء مهلة API
- تنسيقات استجابة غير صالحة
- أخطاء محددة للخدمة

## ملاحظات الأمان
- لا يتم تخزين مفاتيح API في الكود أبدًا
- يتم طلب المفاتيح في وقت التشغيل
- تستخدم جميع طلبات API HTTPS الآمنة
- تحدّ حدود المهلة من طلبات المعلق

</div>
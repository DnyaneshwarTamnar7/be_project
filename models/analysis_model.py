def open_question(text,analysis_model):
    from transformers import AutoTokenizer, AutoModelForSequenceClassification
    from scipy.special import softmax
    # text = "I woke up fresh today"
    #preprocessed text
    text_words = []
    for word in text.split(' '):
        if word.startswith('@') and len(word)>1:
            word = '@user'
        elif word.startswith('http'):
            word = 'http'
        text_words.append(word)
    text_proc = " ".join(text_words)
    # print(text_proc)

    #load the model and tokenizer
    

    model = AutoModelForSequenceClassification.from_pretrained(analysis_model)
    tokenizer = AutoTokenizer.from_pretrained(analysis_model)
    lables=['Negative','Neutral','Positive']

#sentimal anylysis

    encoded_text=tokenizer(text_proc,return_tensors='pt')
    # print(encoded_text)

    output=model(encoded_text['input_ids'],encoded_text['attention_mask'])

    output=model(**encoded_text)
    #print(output)

    scores=output[0][0].detach().numpy()

    scores=softmax(scores)
    # print(scores)
    sum = -1
    index = None
    for i in range(len(scores)):
        l=lables[i]
        s=scores[i]
        if s>sum:
            sum = s
            index = i
        # print(l,s)
    return lables[index]



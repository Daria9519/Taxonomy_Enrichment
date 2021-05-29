import pandas as pd
import re
import emoji


def clean_input_text(df, column_name: str):
    train_df = pd.DataFrame(columns=[column_name])
    train_df[column_name] = df[column_name]
    assert len(train_df) == len(df)
    text_list = []
    for text in train_df[column_name]:
        text_clean = re.compile(r'[.+-,!"*#$%&’(),/:;<=>?@/\^_`-·]')
        num = re.compile(r'\d+')

        emoji_pattern = re.compile("["
                                   u"\U0001F600-\U0001F64F"  # emoticons
                                   u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                   u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                   u"\U00002702-\U000027B0"
                                   u"\U000024C2-\U0001F251"
                                   "]+", flags=re.UNICODE)

        allchars = [str for str in text]
        emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
        clean_text = ' '.join([str for str in text.split() if not any(i in str for i in emoji_list)])

        new_text = emoji_pattern.sub(r'', clean_text)
        cln_text = text_clean.sub(r'', new_text)
        cl_text = num.sub(r'', cln_text)
        c_text = cl_text.replace('/', '')
        low_text = c_text.lower()  # .replace('\n', '')

        text_list.append(str(low_text))
    return text_list


def convert_into_train_file(df, column_name: str, text_name: str):
    text_list = clean_input_text(df, column_name)
    text_list_df = pd.DataFrame(text_list, columns=[column_name])
    assert len(text_list_df) == len(df)

    with open(text_name, "w", encoding='utf-8') as output:
        output.write(text_list_df.to_string(index=False, header=False, columns=[column_name]))

    return print(f'The document was written successfuly!')
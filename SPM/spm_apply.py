import time
import sentencepiece as spm

def spm_apply(input_text: list, model_name: str, alpha=0.1, enable_sampling=True, nbest_size=2):
    '''If you use unigram model, you should define the variable model_name = 'm_unigram.model' '''

    sp = spm.SentencePieceProcessor()

    global time

    start_time = time.time()
    sp.load(model_name)
    subword_tokens_list = []
    subword_vectors_list = []


    for text in input_text:
        subword_tokens_list.append(sp.encode_as_pieces(text))
        subword_vectors_list.append(sp.encode(str(text), alpha=0.1))

    end_time = time.time()
    work_time = end_time - start_time
    print(f'Time: {work_time}')
    assert len(subword_tokens_list) > 0
    print(f'List with subword was written successfuly!')
    print(f'Len of input_text: {len(input_text)}')
    print(f'Len of subword_tokens_list: {len(subword_tokens_list)}' + '\n')
    return subword_tokens_list, subword_vectors_list
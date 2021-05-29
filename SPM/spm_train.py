import time
import sentencepiece as spm


def spm_train(input_file: str,
              model_type: str,
              vocab_size: str,
              model_prefix='m',
              character_coverage='1.0',
              normalization_rule_name='nfkc_cf'
              ):
    '''--input: one-sentence-per-line raw corpus file. No need to run tokenizer, normalizer or preprocessor.
            By default, SentencePiece normalizes the input with Unicode NFKC. You can pass a comma-separated list of files.

        --model_prefix: output model name prefix. .model and .vocab are generated.

        --vocab_size: vocabulary size, e.g., 8000, 16000, or 32000

        --character_coverage: amount of characters covered by the model, good defaults are: 0.9995
            for languages with rich character set like Japanse or Chinese and 1.0 for other languages with small character set.

        --model_type: model type. Choose from unigram (default), bpe, char, or word.
            The input sentence must be pretokenized when using word type.

        --normalization_rule_name: SentencePiece provides the following pre-defined normalization rule.
                                   It is recommended to use one of them unless you have any special reasons.
            nmt_nfkc: NFKC normalization with some additional normalization around spaces. (default)
            nfkc: original NFKC normalization.
            nmt_nfkc_cf: nmt_nfkc + Unicode case folding (mostly lower casing)
            nfkc_cf: nfkc + Unicode case folding.
            identity: no normalization

        ---There are two types of special tokens:

        --user defined symbols: Always treated as one token in any context. These symbols can appear in the input sentence.
        --control symbol: We only reserve ids for these tokens. Even if these tokens appear in the input text,
                          they are not handled as one token. User needs to insert ids explicitly after encoding.'''

    global time

    start_time = time.time()

    print(f'Model: {model_prefix}')

    spm.SentencePieceTrainer.train(
        f'--input={input_file} --model_type={model_type} --model_prefix={model_prefix} --vocab_size={vocab_size} --model_type={model_type} --normalization_rule_name={normalization_rule_name} --user_defined_symbols="<e1>","</e1>","<e2>","</e2>"')
    end_time = time.time()
    time_general = end_time - start_time
    print("Time:", time_general)
    return ('The model was trained saccessfuly')
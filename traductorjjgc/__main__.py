from translate import Translator
import click


@click.command()
@click.argument('string_en')
def main(string_en):
    print("EN -> ES")

    trasnlator = Translator('es', from_lang='en')
    stringEs = trasnlator.translate(string_en)

    print(f'{string_en} -> {stringEs}')

if __name__ == '__main__':
    main()

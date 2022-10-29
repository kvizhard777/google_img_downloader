from icrawler.builtin import GoogleImageCrawler

def google_img_downloader():
    filters = dict(
        type='photo',                         # тип файла (photo, face, clipart и т.д.)
        size='large',                         # размер изображения (=1920x1080, large, icon, small и т.д.)
        # license='noncommercial',              # лицензия (commercial, noncommercial)
        # color='blackandwhite',                # цвет картинки
        # date=((2020, 1, 1), (2022, 9, 4))     # дата или промежуток
    )
    crawler = GoogleImageCrawler(storage={'root_dir': './img'})

    # keyword - ключевое слово, max_num - максимальное количество скачиваемых картинок
    # min_size - минимально допустимое разрешение картинки, overwrite - возможность перезаписывать скачанные файлы
    # по дефолту overwrite стоит на False, max_size - максимально допустимое разрешение картинки

    # crawler.crawl(keyword='mr.robot', max_num=5)
    # crawler.crawl(keyword='programming', max_num=5, min_size=(1000, 1000), overwrite=True)

    crawler.crawl(
        keyword='Miami Florida',
        max_num=5,
        min_size=(1000, 1000),
        overwrite=True,
        file_idx_offset='auto',
        filters=filters
    )

def main():
    google_img_downloader()

if __name__ == '__main__':
    main()
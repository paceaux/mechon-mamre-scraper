from fetchPages import get_page

def get_book_data_from_html(html, url):
    book_data = {}

    # Find the script tag that calls 'chapters' function
    script_tags = html.find_all('script')
    for script in script_tags:
        script_content = script.get_text()
        if script_content and 'chapters(' in script_content:
            break
    else:
        raise Exception('No chapters function found in script tags')

    # Extract arguments from the script content
    args_str = script_content.strip()[9:-1]  # Remove 'chapters(' and ')'
    args = [arg.strip().strip("'\"") for arg in args_str.split(',')]

    # Debug print to check the arguments
    # print("Script content:", script_content)
    # print("Arguments:", args)

    url_prefix = args[0]
    start_chapter = int(args[1])
    end_chapter = int(args[2])

    if len(args) > 5:
        book_name = args[5]
    else:
        #book_name = 'Unknown'
        raise Exception('Book name not found in script arguments')

    canonicalBookName = book_name
    book_data['canonicalBookName'] = canonicalBookName

    # Generate chapter links
    chapters = {}
    base_url = '/'.join(url.split('/')[:-1]) + '/'

    for chapter_num in range(start_chapter, end_chapter + 1):
        chapter_link = get_chapter_link(url_prefix, chapter_num, base_url)
        chapters[str(chapter_num)] = chapter_link

    book_data['chapters'] = chapters

    return book_data

def get_chapter_link(url_prefix, chapter_num, base_url):
    if url_prefix == 'pt26':  # Psalms
        if chapter_num <= 99:
            chapter_str = str(chapter_num).zfill(2)
            chapter_link = f"{base_url}{url_prefix}{chapter_str}.htm"
        else:
            # For chapters >= 100
            letters = ['a', 'b', 'c', 'd', 'e']
            index = min((chapter_num - 100) // 10, 4)  # Ensure index doesn't exceed 4
            letter = letters[index]
            digit = (chapter_num - 100) % 10
            chapter_link = f"{base_url}{url_prefix}{letter}{digit}.htm"
    else:
        # For other books
        chapter_str = str(chapter_num).zfill(2)
        chapter_link = f"{base_url}{url_prefix}{chapter_str}.htm"
    return chapter_link

def get_book_data(url):
    try:
        pageHtml = get_page(url)
        book_data = get_book_data_from_html(pageHtml, url)
        return book_data
    except Exception as error:
        print('Error in get_book_data:', error)
        return {}

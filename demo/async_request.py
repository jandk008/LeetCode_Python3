import asyncio
import logging
import re
import sys

import aiofiles
import aiohttp
from aiohttp import ClientSession

HREF_PATTERN = re.compile(r'href="(.*)"')

logging.basicConfig(format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
                    level=logging.INFO, datefmt="%H:%M:%S", stream=sys.stdout, )
logger = logging.getLogger('async_request')


async def fetch_html(url: str, session: ClientSession) -> str:
    response = await session.request(method='GET', url=url)
    response.raise_for_status()
    return await response.text()


async def parse_href(html: str, url: str) -> list:
    parsed_urls = []
    found_urls = HREF_PATTERN.findall(html)
    import urllib.parse
    import urllib.error
    for _ in found_urls:
        try:
            pure_link = urllib.parse.urljoin(url, _)
        except urllib.error.URLError:
            logger.error('Error parsing URL: %s', _)
        else:
            parsed_urls.append(pure_link)
    return parsed_urls


async def write_url(file_path: str, url: str,
                    client_session: ClientSession) -> None:
    logger.info('fetch html from %s', url)
    try:
        html = await fetch_html(url, client_session)
    except (aiohttp.ClientError, aiohttp.ClientResponseError) as e:
        logger.error('Encountering http error when fetching %s', url, e)
    else:
        parsed_urls = await parse_href(html, url)
        async with aiofiles.open(file_path, 'a') as output_file:
            logger.info('start to write parsed url retrieved from %s', url)
            for _ in parsed_urls:
                logger.info('writing %s to %s', _, file_path)
                await output_file.write(f'{url}\t{_}\n')
            logger.info('writing parsed urls from %s completed', url)


async def write_bulk_crawled_url(file_path: str, urls: set) -> None:
    import time
    now = time.perf_counter()
    async with ClientSession() as client_session:
        tasks = []
        for _ in urls:
            tasks.append(write_url(file_path, _, client_session))
        logger.info('start to await tasks to complete')
        await asyncio.gather(*tasks)
    logger.info('Complete all tasks within %f seconds',
                time.perf_counter() - now)


if __name__ == '__main__':
    print('path:', __file__)
    with open('urls.txt', 'r') as inputFile:
        urls = set(map(str.strip, inputFile))

    output_file_path = 'results.txt'
    with open(output_file_path, 'w') as output:
        output.write('source_url \t parsed_url\n')
    asyncio.run(write_bulk_crawled_url(output_file_path, urls))

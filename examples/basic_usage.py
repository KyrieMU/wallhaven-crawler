from wallhaven_crawler import PowerfulCrawler

def main():
    # 使用示例 - 爬取Wallhaven网站的图片
    # 注意：实际使用时请遵守网站的robots.txt规则和相关法律法规
    
    # 需要登录的URL
    target_url = "https://wallhaven.cc/search?categories=010&purity=001&sorting=hot&order=desc&ai_art_filter=1&page=2" 
    save_directory = "downloaded_images"
    
    # 填入你的Wallhaven账号和密码
    username = "your_username"  # 替换为你的用户名
    password = "your_password"  # 替换为你的密码
    
    crawler = PowerfulCrawler(target_url, save_directory, username=username, password=password)
    # 设置最大爬取10个页面，最大下载100张图片
    crawler.start(max_pages=10, max_images=100)

if __name__ == "__main__":
    main()
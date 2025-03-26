# Wallhaven Crawler

一个强大的 Wallhaven 网站爬虫库，可以轻松下载高质量壁纸。

## 安装

```bash
pip install wallhaven-crawler

# Wallhaven 爬虫库使用教程

## 简介

Wallhaven Crawler 是一个功能强大的 Python 库，专为爬取 Wallhaven 网站上的高质量壁纸而设计。通过简单的配置，你可以轻松下载各种分类的壁纸，并自定义保存位置。

![Wallhaven 网站截图](https://wallhaven.cc/images/layout/logo.png)

## 特点

- 🚀 **高效并行下载**：利用多线程技术，大幅提升下载速度
- 🔐 **支持登录**：可访问需要账号的 NSFW 内容
- 🔄 **智能分页**：自动处理分页，无需手动干预
- 📂 **自定义保存**：灵活设置图片保存位置
- 🔍 **精准爬取**：支持按分类、标签、排序方式等筛选壁纸

## 安装方法

```bash
pip install wallhaven-crawler
```

## 基本使用

### 快速开始

```python
from wallhaven_crawler import PowerfulCrawler

# 初始化爬虫
crawler = PowerfulCrawler(
    base_url="https://wallhaven.cc/search?categories=010&purity=100",
    save_dir="我的壁纸"
)

# 开始爬取
crawler.start(max_pages=5, max_images=20)
```

### 需要登录的内容

```python
from wallhaven_crawler import PowerfulCrawler

# 初始化爬虫（带登录信息）
crawler = PowerfulCrawler(
    base_url="https://wallhaven.cc/search?categories=010&purity=001",
    save_dir="NSFW壁纸",
    username="你的用户名",
    password="你的密码"
)

# 开始爬取
crawler.start(max_pages=10, max_images=100)
```

## 高级配置

### URL 参数说明

Wallhaven 的搜索 URL 可以包含多种参数，以下是常用参数的说明：

| 参数 | 说明 | 示例值 |
|------|------|--------|
| categories | 壁纸分类 (General/Anime/People) | 111 = 全部, 100 = 仅General |
| purity | 内容分级 (SFW/Sketchy/NSFW) | 100 = 仅SFW, 111 = 全部 |
| sorting | 排序方式 | date_added, relevance, random, views, favorites, toplist |
| order | 排序顺序 | desc, asc |
| q | 搜索关键词 | nature, anime, cyberpunk |
| ai_art_filter | AI生成内容过滤 | 0 = 显示AI内容, 1 = 过滤AI内容 |

### 完整示例

```python
from wallhaven_crawler import PowerfulCrawler

# 搜索带有"cyberpunk"标签的动漫壁纸，按热度排序
crawler = PowerfulCrawler(
    base_url="https://wallhaven.cc/search?q=cyberpunk&categories=010&purity=100&sorting=toplist&order=desc",
    save_dir="赛博朋克壁纸",
    max_workers=15  # 增加并行下载线程数
)

# 限制下载数量
crawler.start(max_pages=20, max_images=200)
```

## 常见问题

### Q: 为什么有些壁纸无法下载？
A: 部分壁纸可能需要登录才能访问，特别是NSFW内容。请确保提供了正确的账号密码。

### Q: 下载速度很慢怎么办？
A: 可以尝试增加 `max_workers` 参数值来提高并行下载数量，但请注意不要设置过高以避免被网站封禁。

### Q: 如何只下载特定分辨率的壁纸？
A: 可以在URL中添加 `resolutions=1920x1080` 参数来筛选特定分辨率的壁纸。

## 注意事项

- 请遵守 Wallhaven 的使用条款和版权规定
- 避免过于频繁的请求，以防IP被临时封禁
- 下载的图片仅供个人使用，请勿用于商业目的

## 贡献与反馈

如果你发现任何问题或有改进建议，欢迎提交 Issue 或 Pull Request。

---

*本库仅用于学习和个人使用，请尊重网站规则和内容版权。*
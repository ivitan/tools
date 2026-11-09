# 实用工具箱 🛠️

![License](https://img.shields.io/badge/license-Apache%202.0-blue)
![Languages](https://img.shields.io/badge/language-HTML-orange)
![Status](https://img.shields.io/badge/status-active-brightgreen)

一个精心设计的在线工具集合，提供实用、高效的日常工具支持。拥有现代化的界面设计、深色/浅色主题切换、响应式布局和流畅的用户体验。

🌐 **在线访问**: [http://t.ivitan.com/](http://t.ivitan.com/)

## ✨ 功能特性

### 🎨 UI/UX 设计
- **主题切换**: 内置深色/浅色两种模式，自动检测系统偏好
- **响应式设计**: 完美适配桌面、平板和手机设备
- **流畅动画**: CSS3 过渡效果，提供舒适的交互体验
- **现代化界面**: 使用 Font Awesome 图标库，清爽简洁的设计风格

### 🔍 搜索功能
- 实时搜索工具
- 支持按工具名称、分类和描述搜索
- 即时过滤显示

### 📱 工具集合

与主页菜单一致，共 8 个工具：

1. **Type Search**（数据处理）— 智能类型检索 & 快速定位
2. **Exchange**（计算工具）— 百分数 · 小数 · 单位互换
3. **Markdown Editor**（编辑工具）— 即时编写与预览
4. **WebUSB Imager**（烧录工具）— 制作启动盘
5. **WebADB**（烧录工具）— android 玩机
6. **Daily Report**（编辑工具）— 日报生成
7. **Airport Information**（数据处理）— 航班节点时间提取
8. **SQLite**（数据库工具）— 数据库读取工具

## 🚀 快速开始

### 本地运行

无需任何构建工具，直接在浏览器中打开 HTML 文件即可使用：

```bash
# 克隆项目
git clone https://github.com/ivitan/tools.git
cd tools

# 使用 Python 启动本地服务器（Python 3）
python -m http.server 8000

# 或使用 Node.js http-server
npx http-server

# 然后访问
# http://localhost:8000
```

### 部署

项目可以部署到任何支持静态文件的服务器：
- GitHub Pages
- Vercel
- Netlify
- 传统虚拟主机
- 云服务（AWS S3、阿里云 OSS 等）

## 📁 项目结构

```
tools/
├── index.html              # 主页 - 工具导航界面
├── CNAME                   # 自定义域名配置
├── README.md               # 项目说明文档
├── .editorconfig           # 编辑器配置
├── LICENSE                 # Apache 2.0 许可证
├── img/                    # 工具图标（SVG）
│
├── TypeSearch/             # Type Search
│   └── index.html
├── Exchange/               # Exchange
│   └── index.html
├── Markdown/               # Markdown Editor
│   └── index.html
├── WebUSB/                 # WebUSB Imager
│   └── index.html
├── android/                # WebADB
│   └── index.html
├── Daily/                  # Daily Report
│   └── index.html
├── Airport/                # Airport Information
│   └── index.html
└── SQLite/                 # SQLite
    └── index.html
```

## 🛠️ 技术栈

- **HTML5**: 语义化标签
- **CSS3**: 
  - CSS 变量（CSS Custom Properties）
  - Flexbox 和 Grid 布局
  - Media Query 响应式设计
  - 过渡和动画效果
- **JavaScript (Vanilla)**:
  - 原生 DOM 操作
  - LocalStorage API
  - 事件监听和处理
- **第三方库**:
  - Font Awesome 6.4.0 (图标)
  - Marked 11.1.1 (Markdown 解析)
  - Highlight.js 11.9.0 (代码高亮)

## 💾 本地存储

项目利用浏览器 LocalStorage API 来存储用户数据，无需后端：

- **主题偏好**: 记忆用户选择的深色/浅色模式
- **Markdown 编辑器内容**: 自动保存编辑的文档
- **编辑器布局**: 保存分隔条的拖拽位置

## 🎨 主题系统

使用 CSS 变量实现灵活的主题切换：

### 浅色模式变量示例
```css
--bg-primary: #f5f7fa
--text-color: #333
--primary-color: #3498db
```

### 深色模式变量示例
```css
--bg-primary: #1a2a6c
--text-color: #e2e8f0
--primary-color: #3b82f6
```

所有颜色通过变量定义，切换主题时只需改变变量值，整个应用自动适配。

## 📖 使用说明

1. 在主页浏览工具卡片，点击需要的工具
2. 使用搜索框快速查找特定工具，或按左侧分类筛选
3. 点击右上角按钮切换深色/浅色主题

## 🌐 浏览器兼容性

- ✅ Chrome/Chromium 60+
- ✅ Firefox 55+
- ✅ Safari 12+
- ✅ Edge 79+
- ✅ 现代移动浏览器

## 📝 许可证

本项目采用 [Apache License 2.0](LICENSE) 许可证。

## 🤝 贡献

欢迎提交 Issue 或 Pull Request！

## 📧 联系方式

- GitHub: [@ivitan](https://github.com/ivitan)
- 网站: [http://t.ivitan.com/](http://t.ivitan.com/)

## 🎯 未来计划

- [ ] 更多实用工具

---

<div align="center">

**Made with ❤️ by ivitan**

⭐ 如果这个项目对你有帮助，请给一个星星支持！

</div>

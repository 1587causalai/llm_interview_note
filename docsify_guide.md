# Docsify 文档网站搭建教程

## 1. 简介

Docsify 是一个轻量级的文档网站生成器，不会生成静态 html 文件，而是在运行时直接解析 Markdown 文件。本教程将指导你如何使用 Docsify 快速搭建项目文档网站。

## 2. 适用场景

- 项目技术文档
- API 接口文档
- 开发指南
- 学习笔记
- 个人知识库

## 3. 环境准备

### 3.1 必需环境
- Node.js (推荐使用 LTS 版本)
- npm (Node.js 包管理器)

### 3.2 安装 Docsify CLI
```bash
npm i docsify-cli -g
```

## 4. 快速开始

### 4.1 初始化项目
```bash
# 创建文档目录
mkdir my-docs
cd my-docs

# 初始化 docsify
docsify init .
```

初始化后将创建以下文件：
- `index.html`: 入口文件
- `README.md`: 主页内容
- `.nojekyll`: 防止 GitHub Pages 忽略下划线开头的文件

### 4.2 本地预览
```bash
docsify serve .
```
访问 http://localhost:3000 查看效果

## 5. 基础配置

### 5.1 配置 index.html
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>项目文档</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify@4/lib/themes/vue.css">
</head>
<body>
  <div id="app"></div>
  <script>
    window.$docsify = {
      name: '项目名称',
      repo: 'your-github-repo',
      loadSidebar: true,
      subMaxLevel: 3,
      search: {
        paths: 'auto',
        placeholder: '搜索',
        noData: '没有结果'
      },
      count:{
        countable: true,
        position: 'top',
        margin: '10px',
        float: 'right',
        fontsize:'0.9em',
        color:'rgb(90,90,90)',
        language:'chinese',
        isExpected: true
      }
    }
  </script>
  <!-- Docsify 核心 -->
  <script src="//cdn.jsdelivr.net/npm/docsify@4"></script>
  <!-- 搜索插件 -->
  <script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/search.min.js"></script>
  <!-- 代码复制 -->
  <script src="//cdn.jsdelivr.net/npm/docsify-copy-code"></script>
  <!-- 代码高亮 -->
  <script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-bash.min.js"></script>
  <script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-json.min.js"></script>
</body>
</html>
```

### 5.2 创建侧边栏 (_sidebar.md)
```markdown
* [首页](/)
* [指南](guide.md)
  * [快速开始](quick-start.md)
  * [详细配置](configuration.md)
* [API 文档](api/)
  * [接口说明](api/overview.md)
  * [接口列表](api/list.md)
```

## 6. 进阶功能

### 6.1 多级目录
```
docs/
  ├── README.md
  ├── guide/
  │   ├── README.md
  │   ├── quick-start.md
  │   └── advanced.md
  └── api/
      ├── README.md
      ├── user.md
      └── product.md
```

### 6.2 常用插件

#### 6.2.1 全文搜索
```html
<script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/search.min.js"></script>
```

#### 6.2.2 图片缩放
```html
<script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/zoom-image.min.js"></script>
```

#### 6.2.3 复制代码
```html
<script src="//cdn.jsdelivr.net/npm/docsify-copy-code"></script>
```

#### 6.2.4 字数统计
```html
<script src="//unpkg.com/docsify-count/dist/countable.js"></script>
```

### 6.3 Markdown 增强
- 支持 Todo List
- 支持表格
- 支持 emoji
- 支持数学公式 (需要额外插件)

## 7. 部署方案

### 7.1 GitHub Pages 自动部署

1. **准备工作**
   - 确保你的仓库中包含以下文件：
     - `index.html`（Docsify 配置文件）
     - `README.md`（首页内容）
     - `_sidebar.md`（如果使用侧边栏）
     - `.nojekyll`（防止 GitHub Pages 忽略下划线开头的文件）

2. **创建 GitHub Actions 工作流**
   在仓库根目录创建 `.github/workflows/deploy.yml` 文件：
   ```yaml
   name: Deploy to GitHub Pages
   
   on:
     push:
       branches:
         - main  # 或者是你的默认分支
   
   jobs:
     deploy:
       runs-on: ubuntu-latest
       steps:
         - name: Checkout
           uses: actions/checkout@v3
   
         - name: Setup Node.js
           uses: actions/setup-node@v3
           with:
             node-version: '16'
   
         - name: Install Dependencies
           run: npm install -g docsify-cli
   
         - name: Build
           run: |
             # 如果需要构建步骤，可以在这里添加
             echo "No build step required for Docsify"
   
         - name: Deploy
           uses: JamesIves/github-pages-deploy-action@v4
           with:
             branch: gh-pages  # 部署到 gh-pages 分支
             folder: .         # 部署整个目录
             clean: true      # 清理旧文件
   ```

3. **启用 GitHub Pages**
   - 进入仓库设置 Settings > Pages
   - Source 选择 "Deploy from a branch"
   - Branch 选择 "gh-pages" 分支，文件夹选择 "/ (root)"
   - 点击 Save

4. **自动部署流程**
   - 当你推送代码到 main 分支时：
     1. GitHub Actions 会自动触发部署工作流
     2. 工作流会创建/更新 gh-pages 分支
     3. GitHub Pages 会自动从 gh-pages 分支部署网站
   - 部署完成后可以通过 `https://<username>.github.io/<repository>` 访问

5. **私有仓库说明**
   - 对于私有仓库，你需要：
     1. 升级到 GitHub Pro/Team/Enterprise
     2. 或者使用其他部署方案（如 Vercel、Netlify）
     3. 或者考虑使用 GitLab（支持私有仓库的 Pages）

6. **自定义域名**（可选）
   - 在仓库设置中添加自定义域名
   - 创建 `CNAME` 文件，内容为你的域名
   - 在域名提供商处添加相应的 DNS 记录

7. **部署检查**
   - 在 Actions 标签页查看部署状态
   - 在 Settings > Pages 查看部署 URL
   - 检查 gh-pages 分支是否正确更新

### 7.2 私有部署
1. 构建 Docker 镜像
```dockerfile
FROM nginx:alpine
COPY . /usr/share/nginx/html
```

2. 运行容器
```bash
docker build -t my-docs .
docker run -p 80:80 my-docs
```

### 7.3 其他部署选项
- Netlify
- Vercel
- GitLab Pages
- 自建服务器

## 8. 最佳实践

### 8.1 目录结构建议
```
project/
  ├── docs/              # 文档目录
  │   ├── index.html     # 入口文件
  │   ├── README.md      # 首页
  │   ├── _sidebar.md    # 侧边栏
  │   ├── _navbar.md     # 导航栏
  │   ├── guide/         # 指南
  │   ├── api/           # API文档
  │   └── assets/        # 资源文件
  └── src/               # 项目源码
```

### 8.2 文档编写建议
- 使用清晰的目录结构
- 保持文档的及时更新
- 添加适当的代码示例
- 使用统一的文档风格
- 添加必要的图片说明

### 8.3 私有项目文档方案
1. 使用 GitLab 自建服务
2. 使用 Nginx 反向代理，添加访问控制
3. 使用 Docker 部署，配置访问权限
4. 使用 VPN 访问控制

## 9. 常见问题

### 9.1 图片路径问题
- 使用相对路径：`./images/pic.png`
- 使用绝对路径：`/images/pic.png`
- 使用图床

### 9.2 部署后刷新 404
添加 Nginx 配置：
```nginx
location / {
  try_files $uri $uri/ /index.html;
}
```

### 9.3 私有部署安全性
1. 添加 Basic Authentication
2. 配置 SSL 证书
3. 设置访问控制策略

## 10. 进阶定制

### 10.1 自定义主题
```css
:root {
  --theme-color: #42b983;
  --sidebar-width: 300px;
}
```

### 10.2 自定义插件
```javascript
window.$docsify.plugins = [].concat(function(hook, vm) {
  hook.beforeEach(function(content) {
    // 在内容渲染之前处理
    return content;
  });
}, window.$docsify.plugins);
```

## 11. 参考资源

- [Docsify 官方文档](https://docsify.js.org/)
- [Docsify GitHub](https://github.com/docsifyjs/docsify/)
- [Awesome Docsify](https://github.com/docsifyjs/awesome-docsify) 
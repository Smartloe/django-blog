# Django博客系统
一个基于Django框架开发的现代化博客系统，使用uv进行项目管理。

## 功能特性

- 📝 文章发布和管理
- 🏷️ 分类管理
- 💬 评论系统
- 🔍 文章搜索
- 📱 响应式设计
- 👤 用户认证（用户/管理员分离）
- 🎨 Bootstrap 5样式
- 🖼️ 图片上传支持
- 📊 浏览统计
- 📄 分页功能
- 🎨 美化的管理后台界面
- 📈 统计仪表盘
- 🎯 自定义管理员导航

## 技术栈

- **后端框架**: Django 5.2.8
- **数据库**: SQLite (开发环境)
- **前端框架**: Bootstrap 5
- **包管理器**: uv
- **图片处理**: Pillow

## 项目结构

```
django-blog/
├── blog/                    # 博客应用
│   ├── migrations/          # 数据库迁移文件
│   ├── templates/blog/      # 模板文件
│   ├── management/commands/ # 管理命令
│   ├── admin.py            # 管理界面配置
│   ├── models.py           # 数据模型
│   ├── views.py            # 视图函数
│   ├── urls.py             # URL配置
│   └── forms.py            # 表单定义
├── blog_project/           # 项目配置
│   ├── settings.py         # 项目设置
│   └── urls.py            # 主URL配置
├── static/                # 静态文件
├── media/                 # 媒体文件
├── templates/             # 模板文件
├── manage.py              # Django管理脚本
├── pyproject.toml         # uv项目配置
└── README.md              # 项目说明
```

## 快速开始

### 环境要求

- Python 3.8+
- uv (最新版本)

### 安装步骤

1. **克隆项目**
   ```bash
   git clone <repository-url>
   cd django-blog
   ```

2. **安装依赖**
   ```bash
   uv sync
   ```

3. **数据库迁移**
   ```bash
   uv run python manage.py migrate
   ```

4. **创建超级用户**
   ```bash
   uv run python manage.py createsuperuser
   ```

5. **创建示例数据（可选）**
   ```bash
   uv run python manage.py create_sample_data
   ```

6. **启动开发服务器**
   ```bash
   uv run python manage.py runserver
   ```

7. **访问应用**
   - 前端: http://127.0.0.1:8000/
   - 用户登录: http://127.0.0.1:8000/login/
   - 用户注册: http://127.0.0.1:8000/register/
   - 管理后台:
     - 默认: http://127.0.0.1:8000/admin/
     - 美化版: http://127.0.0.1:8000/admin-custom/
     - 管理员导向: http://127.0.0.1:8000/admin-login/
   - 管理员账号: admin / admin123

## 使用说明

### 管理后台

1. 使用创建的超级用户账号登录管理后台
2. 在"分类"模块中创建文章分类
3. 在"文章"模块中发布新文章
4. 在"评论"模块中管理用户评论

### 前台功能

- **首页**: 显示最新文章和分类列表
- **文章列表**: 分页显示所有已发布文章
- **文章详情**: 显示文章内容和评论
- **分类浏览**: 按分类查看相关文章
- **搜索功能**: 搜索文章标题和内容
- **评论互动**: 登录用户可以发表评论

## 开发指南

### 添加新功能

1. 在 `blog/models.py` 中定义数据模型
2. 运行 `makemigrations` 和 `migrate` 更新数据库
3. 在 `blog/views.py` 中实现视图逻辑
4. 在 `blog/urls.py` 中配置URL路由
5. 在 `blog/templates/blog/` 中创建模板
6. 在 `blog/admin.py` 中注册管理界面

### 自定义样式

- 修改 `static/css/` 中的CSS文件
- 在模板中引入自定义样式
- 可以使用Bootstrap 5的组件和工具类

## 部署指南

### 生产环境配置

1. **设置环境变量**
   ```bash
   export DEBUG=False
   export SECRET_KEY=your-secret-key
   export ALLOWED_HOSTS=yourdomain.com
   ```

2. **数据库配置**
   - 修改 `settings.py` 中的数据库配置
   - 使用PostgreSQL或MySQL生产数据库

3. **静态文件处理**
   ```bash
   uv run python manage.py collectstatic
   ```

4. **Web服务器**
   - 推荐使用Nginx + Gunicorn
   - 配置SSL证书

## 贡献指南

1. Fork项目
2. 创建功能分支
3. 提交更改
4. 推送到分支
5. 创建Pull Request

## 许可证

MIT License

## 联系方式

如有问题或建议，请通过以下方式联系：
- 提交Issue
- 发送邮件

## 🎨 管理后台美化

### 美化特性

本项目提供了两套管理后台界面：

#### 1. 默认Django管理后台
- 访问地址: http://127.0.0.1:8000/admin/
- 特点: Django原生管理界面
- 适用: 快速数据管理

#### 2. 美化自定义管理后台  
- 访问地址: http://127.0.0.1:8000/admin-custom/
- 特点: 现代化UI设计

### 🎯 美化功能
- **📈 统计仪表盘**: 显示文章、分类、评论统计
- **🎨 现代化设计**: 渐变色背景、圆角设计、阴影效果
- **✨ 动画效果**: 悬停动画、过渡效果
- **📱 响应式布局**: 适配各种屏幕尺寸
- **🎯 自定义导航**: 友好的用户界面
- **📊 数据可视化**: 直观的统计卡片
- **🔧 快捷操作**: 便捷的常用功能入口

### 🎨 设计元素
- **配色方案**: 蓝紫色渐变主题
- **图标系统**: FontAwesome 6.0图标
- **交互反馈**: 悬停状态、点击效果
- **信息提示**: 友好的错误和成功提示
- **操作按钮**: 现代化按钮设计

### 📱 访问方式
```bash
# 美化管理后台
http://127.0.0.1:8000/admin-custom/

# 默认管理后台  
http://127.0.0.1:8000/admin/

# 管理员登录导向页面
http://127.0.0.1:8000/admin-login/
```

## 更新日志

### v1.1.0
- ✨ 新增美化管理后台界面
- 📈 统计仪表盘功能
- 🎨 现代化UI设计
- 👤 用户/管理员登录分离
- 🎯 自定义导航和快捷操作
- 📱 响应式布局优化

### v1.0.0
- 初始版本发布
- 基础博客功能
- 管理后台
- 响应式设计

**使用Python的Fabric库把常用的发布操作封装在一起，本地可用pip一键安装，之后部署就可以一键执行了**

## 一、快速使用

### 安装
可以先把本地的ssh公钥设置在git上自己的账号中，免去输入用户名和密码
```
pip install fabric==1.14.1
pip install git+https://github.com/mrcharleshu/auto-deploy-fabric.git
```

### 卸载
```
pip uninstall auto-deploy-fabric
```

### 四个部署命令
- deploy_test_engine
- deploy_test_stats_api
- deploy_staging_engine
- deploy_staging_stats_api


## 二、本地使用
### 全局安装`virtualenv`
```
pip install virtualenv
```

### 初始化环境
```
virtualenv --no-site-packages venv
source venv/bin/activate
```

### 安装依赖
```
pip install -r requirements.txt
```

### 退出环境
```
deactivate
```

### 执行task
```
fab deploy_test_engine
fab do_deploy_task:project='engine',branch='develop'
```

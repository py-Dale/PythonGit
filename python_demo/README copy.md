### remark

1. 安装虚拟环境

   ``` shell
   # 其中venv 为虚拟环境文件夹名
   python -m virtualenv --no-site-packages venv
    python -m virtualenv  venv
   ```

2. 切换到虚拟环境

   ``` shell
   # windows
   venv\Scripts\activate.bat
   # mac & linux
   source tutorial-env/bin/activate
   ```

3. 切换回全局环境

   ``` shell
   # windows
   venv\Scripts\deactivate.bat
   # mac & linux
   deactivate
   ```

4. 从包安装依赖信息安装包

   ``` shell
   # requirements.txt 为记录使用的包的信息
   pip install -r requirements.txt
   ```

5. 当给项目添加了新的包时，需要更新到requirements.txt

   ``` shell
   pip freeze > requirements.txt
   ```

ps: 注意使用的pip为全局的还是虚拟的，可用以下命令查看

``` shell
pip -v
```



#### 部署

需要排除以下文件

- __pycache__
- .vscode
- logs
- resource
- test
- venv (虚拟环境文件夹)。 服务器上面的是另一个虚拟环境。
- ...

当添加了新包，需向服务器上的项目的venv虚拟环境添加










配置语言 
Ctrl+Shift+P
Configure Language



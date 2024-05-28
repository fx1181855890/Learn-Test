# Allure

## GitHub

下载并添加到环境变量

[https://github.com/allure-framework/allure2](https://github.com/allure-framework/allure2)

## Python

1. **安装 Allure**：
   ```sh
   pip install allure-pytest
   ```

2. **运行测试并生成报告**：
   ```sh
   pytest --alluredir=./allure-results
   ```

3. **生成并查看报告**：
   ```sh
   allure serve ./allure-results
   ```
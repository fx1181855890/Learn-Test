# Allure

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
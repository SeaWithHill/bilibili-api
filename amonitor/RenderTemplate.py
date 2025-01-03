import datetime
from jinja2 import Environment, FileSystemLoader

def export_ups_list_md(templateDir, upsList,outputDir) -> None:
    """
    导出更新信息到markdown文件

    Args:
        templateDir   (str): 模板目录位置

        upsList (List): 更新文件
    """
    # 创建一个Environment对象，指定模板文件所在的目录
    env = Environment(loader=FileSystemLoader(templateDir))
    # 加载模板文件
    template = env.get_template('dailythink.md')
    # 渲染模板，传入实际的值
    rendered = template.render(upsList=upsList)
    filename = outputDir + datetime.datetime.now().strftime('%Y-%m-%d') + '.md'
    # 将渲染后的结果写入文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(rendered)

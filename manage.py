#encoding: utf-8

from flask_migrate import Migrate,MigrateCommand
from zlktqa import app
from flask_script import Manager
from exts import db
import config
from models import UserModel,QuestionModel,AnswerModel

app.config.from_object(config)
db.init_app(app)

#创建命令管理器
manager = Manager(app)
# 绑定app到db
migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)

if __name__ == "__main__":
    manager.run()



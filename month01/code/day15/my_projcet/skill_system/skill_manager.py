# from skill_system.skill_deployer import SkillDeployer

import skill_system

class SKillManager:
    def func01(self):
        print("func01执行喽")

# deployer = SkillDeployer()
# deployer.func02()

# 必须在__init__.py中配置
# import skill_system.skill_deployer

deployer = skill_system.skill_deployer.SkillDeployer()
deployer.func02()
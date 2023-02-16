import yaml
from faker import Faker

from utils.path_handle import data_dir


def creat_member_data():
    write_file = f"{data_dir}/member_data.yaml"
    member_data = {"add": {"P0": {}}, "del": {"P0": {}}}
    fake = Faker(locale='zh_CN')
    member_data_add_p0_datas = []
    member_data_del_p0_datas = []
    member_data_add_p0_ids = []
    member_data_del_p0_ids = []
    for i in range(10):
        name = fake.name_male()
        phone_num = fake.phone_number()
        member_data_add_p0_datas.append([name, phone_num, "添加成功"])
        member_data_del_p0_datas.append([name])
        member_data_add_p0_ids.append(f"{name}_{phone_num}_test_add_data")
        member_data_del_p0_ids.append(f"{name}_test_del_data")
    member_data["add"]["P0"]["datas"] = member_data_add_p0_datas
    member_data["add"]["P0"]["ids"] = member_data_add_p0_ids
    member_data["del"]["P0"]["datas"] = member_data_del_p0_datas
    member_data["del"]["P0"]["ids"] = member_data_del_p0_ids

    with open(write_file, "w") as df:
        yaml.safe_dump(member_data, df, default_flow_style=False, encoding='utf-8', allow_unicode=True)


def get_name_and_phonenum_yaml_file():
    read_file = f"{data_dir}/member_data.yaml"
    with open(read_file) as rf:
        return yaml.safe_load(rf)


if __name__ == '__main__':
    # print(get_name_and_phonenum_yaml_file())
    creat_member_data()
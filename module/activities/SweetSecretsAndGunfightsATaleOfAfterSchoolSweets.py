import importlib
import time
from core import color, picture, image
from module import main_story
from module.explore_normal_task import common_gird_method


def implement(self):
    times = preprocess_activity_sweep_times(self.config["activity_sweep_times"])
    region = preprocess_activity_region(self.config["activity_sweep_task_number"])
    self.logger.info("activity sweep task number : " + str(region))
    self.logger.info("activity sweep times : " + str(times))
    if len(times) > 0:
         sweep(self, region, times)
    exchange_reward(self)
    return True


def preprocess_activity_region(region):
    if type(region) is int:
        return [region]
    if type(region) is str:
        region = region.split(",")
        for i in range(0, len(region)):
            region[i] = int(region[i])
        return region
    if type(region) is list:
        for i in range(0, len(region)):
            if type(region[i]) is int:
                continue
            region[i] = int(region[i])
        return region


def preprocess_activity_sweep_times(times):
    if type(times) is int:
        return [times]
    if type(times) is float:
        return [times]
    if type(times) is str:
        times = times.split(",")
        for i in range(0, len(times)):
            if '.' in times[i]:
                times[i] = min(float(times[i]), 1.0)
            elif '/' in times[i]:
                temp = times[i].split("/")
                times[i] = min(int(temp[0]) / int(temp[1]), 1.0)
            else:
                times[i] = int(times[i])
        return times
    if type(times) is list:
        for i in range(0, len(times)):
            if type(times[i]) is int:
                continue
            if '.' in times[i]:
                times[i] = min(float(times[i]), 1.0)
            elif '/' in times[i]:
                temp = times[i].split("/")
                times[i] = min(int(temp[0]) / int(temp[1]), 1.0)
        return times


def get_stage_data():
    module_path = 'src.explore_task_data.activities.SweetSecretsAndGunfightsATaleOfAfterSchoolSweets'
    stage_module = importlib.import_module(module_path)
    stage_data = getattr(stage_module, 'stage_data', None)
    return stage_data


def sweep(self, number, times):
    self.quick_method_to_main_page()
    to_activity(self, "mission", True, True)
    ap = self.get_ap()
    sweep_one_time_ap = [0, 10, 10, 10, 10, 15, 15, 15, 15, 20, 20, 20, 20]
    for i in range(0, min(len(number), len(times))):
        sweep_times = times[i]
        if type(sweep_times) is float:
            sweep_times = int(ap * sweep_times / sweep_one_time_ap[number[i]])
        click_times = sweep_times-1
        duration = 1
        if sweep_times > 50:
            sweep_times = int(ap / sweep_one_time_ap[number[i]])
            click_times = int(sweep_times / 2) + 1
            duration = 0.3
        if sweep_times <= 0:
            self.logger.warning("inadequate ap")
            continue
        self.logger.info("Start sweep task " + str(number[i]) + " :" + str(sweep_times) + " times")
        to_mission_task_info(self, number[i])
        res = color.check_sweep_availability(self)
        if res == "sss":
            self.click(1032, 299, count=click_times, duration=duration, wait_over=True)
            res = start_sweep(self, True)
            if res == "inadequate_ap":
                self.logger.warning("inadequate ap")
                return True
            elif res == "sweep_complete":
                self.logger.info("Current sweep task " + str(number[i]) + " :" + str(sweep_times) + " times complete")
                if i != len(number) - 1:
                    to_activity(self, "mission", True, True)
        elif res == "pass" or res == "no-pass":
            self.logger.warning("task not sss, sweep unavailable")
            continue
    return True


def explore_story(self):
    self.quick_method_to_main_page()
    to_activity(self, "story", True, True)
    last_target_task = 1
    total_stories = 8
    self.stage_data = get_stage_data()
    while self.flag_run:
        plot = to_story_task_info(self, last_target_task)
        if plot == "normal_task_task-info":
            res = color.check_sweep_availability(self)
        elif plot == "main_story_episode-info":
            if not color.judge_rgb_range(self, 362, 322, 232, 255, 219, 255, 0, 30):
                res = "sss"
            else:
                res = "no-pass"
        while res == "sss" and last_target_task <= total_stories - 1:
            self.logger.info("Current story sss check next story")
            self.click(1168, 361, duration=1.5, wait_over=True)
            last_target_task += 1
            plot = picture.co_detect(self, img_ends=["normal_task_task-info", "main_story_episode-info"])
            if plot == "normal_task_task-info":
                res = color.check_sweep_availability(self)
            elif plot == "main_story_episode-info":
                if not color.judge_rgb_range(self, 362, 322, 232, 255, 219, 255, 0, 30):
                    res = "sss"
                else:
                    res = "no-pass"
        if last_target_task == total_stories and res == "sss":
            self.logger.info("All STORY SSS")
            return True
        start_story(self, last_target_task)
        to_activity(self, "mission", True)
        to_activity(self, "story", True, True)


def start_story(self, i):
    img_possibles = {
        "normal_task_task-info": (940, 538),
        "plot_menu": (1205, 34),
        "plot_skip-plot-button": (1213, 116),
        "plot_skip-plot-notice": (766, 520),
        "main_story_episode-info": (629, 518),
    }
    rgb_ends = [
        "formation_edit1",
        "reward_acquired"
    ]
    img_ends = "normal_task_task-wait-to-begin-feature"
    res = picture.co_detect(self, rgb_ends, None, img_ends, img_possibles, skip_first_screenshot=True)
    if res == "formation_edit1":
        start_fight(self, 1)
        main_story.auto_fight(self)
    elif res == "reward_acquired":
        pass
    else:
        common_gird_method(self, get_stage_data()["story" + str(i)])
        main_story.auto_fight(self)
    return


def start_fight(self, i):
    rgb_possibles = {"formation_edit" + str(i): (1156, 659)}
    rgb_ends = "fighting_feature"
    picture.co_detect(self, rgb_ends, rgb_possibles, skip_first_screenshot=True)


def explore_mission(self):
    self.quick_method_to_main_page()
    to_activity(self, "mission", True, True)
    last_target_mission = 1
    total_missions = 12
    characteristic = [
        'pierce1',
        'burst1',
        'pierce1',
        'pierce1',
        'burst1',
        'burst1',
        'pierce1',
        'pierce1',
        'burst1',
        'burst1',
        'pierce1',
        'pierce1'
    ]
    while last_target_mission <= total_missions and self.flag_run:
        to_mission_task_info(self, last_target_mission)
        res = color.check_sweep_availability(self)
        while res == "sss" and last_target_mission <= total_missions - 1 and self.flag_run:
            self.logger.info("Current task sss check next task")
            self.click(1168, 353, duration=1, wait_over=True)
            last_target_mission += 1
            image.detect(self, "normal_task_task-info")
            res = color.check_sweep_availability(self)
        if last_target_mission == total_missions and res == "sss":
            self.logger.info("All MISSION SSS")
            return True
        number = self.config[characteristic[last_target_mission - 1]]
        self.logger.info("according to config, choose formation [ " + str(number) + " ]")
        to_formation_edit_i(self, number, (940, 538), True)
        start_fight(self, number)
        main_story.auto_fight(self)
        to_activity(self, "story")
        to_activity(self, "mission", True, True)


def explore_challenge(self):
    self.quick_method_to_main_page()
    to_activity(self, "challenge", True, True)
    tasks = [
        "challenge2_sss",
        "challenge2_task",
        "challenge4_sss",
        "challenge4_task",
    ]
    stage_data = get_stage_data()
    for i in range(0, len(tasks)):
        self.logger.info("Start challenge task [ " + tasks[i] + " ]")
        data = tasks[i].split("_")
        task_number = int(data[0].replace("challenge", ""))
        to_challenge_task_info(self, task_number)
        current_task_stage_data = stage_data[tasks[i]]
        need_fight = False
        if "task" in data:
            need_fight = True
        elif "sss" in data:
            res = color.check_sweep_availability(self)
            if res == "sss":
                self.logger.info("Challenge " + str(task_number) + " sss no need to fight")
                to_activity(self, "challenge", True)
                i += 1
                continue
            elif res == "no-pass" or res == "pass":
                need_fight = True
        if need_fight:
            common_gird_method(self, current_task_stage_data)
            i += 1
        main_story.auto_fight(self)
        if self.config['manual_boss']:
            self.click(1235, 41)
        to_activity(self, "mission", True)
        to_activity(self, "challenge", True)


def to_activity(self, region, skip_first_screenshot=False, need_swipe=False):
    task_info = {
        'CN': (1087, 141),
        'Global': (1128, 141),
        'JP': (1126, 115)
    }
    img_possibles = {
        "main_page_get-character": (640, 360),
        "activity_enter1": (1196, 195),
        "activity_enter2": (100, 149),
        "activity_enter3": (218, 530),
        "activity_get-collectable-item1": (508, 505),
        "activity_get-collectable-item2": (505, 537),
        'activity_fight-success-confirm': (640, 663),
        "plot_menu": (1205, 34),
        "plot_skip-plot-button": (1213, 116),
        "purchase_ap_notice": (919, 168),
        'purchase_ap_notice-localized': (919, 168),
        "plot_skip-plot-notice": (766, 520),
        "normal_task_help": (1017, 131),
        "normal_task_task-info": task_info[self.server],
        "activity_play-guide": (1184, 152),
        'main_story_fight-confirm': (1168, 659),
        "main_story_episode-info": (917, 161),
        'normal_task_prize-confirm': (776, 655),
        'normal_task_fail-confirm': (643, 658),
        'normal_task_task-finish': (1038, 662),
        'normal_task_fight-confirm': (1168, 659),
        "normal_task_sweep-complete": (643, 585),
        "normal_task_start-sweep-notice": (887, 164),
        'normal_task_skip-sweep-complete': (643, 506),
        'normal_task_fight-complete-confirm': (1160, 666),
        'normal_task_reward-acquired-confirm': (800, 660),
        'normal_task_mission-conclude-confirm': (1042, 671),
        "activity_exchange-confirm": (673, 603),
        "activity_joint-task-boss-info": (916, 120),
        "activity_joint-task-menu-task-info": (1157, 115),
        "activity_joint-task-menu": (63, 40),
        "activity_exchange-menu": (63, 40),
    }
    img_ends = "activity_menu"
    picture.co_detect(self, None, None, img_ends, img_possibles, skip_first_screenshot=skip_first_screenshot)
    if region is None:
        return True
    rgb_lo = {
        "mission": 863,
        "story": 688,
        "challenge": 1046,
    }
    click_lo = {
        "mission": 1027,
        "story": 848,
        "challenge": 1196,
    }
    while self.flag_run:
        if not color.judge_rgb_range(self, rgb_lo[region], 114, 20, 60, 40, 80, 70, 116):
            self.click(click_lo[region], 87)
            time.sleep(self.screenshot_interval)
            self.latest_img_array = self.get_screenshot_array()
        else:
            if need_swipe:
                if region == "mission":
                    self.swipe(919, 155, 943, 720, duration=0.05, post_sleep_time=1)
                    self.swipe(919, 155, 943, 720, duration=0.05, post_sleep_time=1)
                elif region == "story":
                    self.swipe(919, 155, 943, 720, duration=0.05, post_sleep_time=1)
            return True


def to_story_task_info(self, number):
    lo = [0, 180, 280, 380, 480, 580, 680, 580, 680]
    if number >= 7:
        self.swipe(916, 667, 916, 0, duration=0.05, post_sleep_time=0.7)
    img_possibles = {'activity_menu': (1124, lo[number])}
    img_ends = [
        "normal_task_task-info",
        "main_story_episode-info"
    ]
    return picture.co_detect(self, None, None, img_ends, img_possibles, True)


def to_mission_task_info(self, number):
    lo = [0, 184, 308, 422, 537, 645]
    index = [1, 2, 3, 4, 5, 4, 5, 1, 2, 3, 4, 5]
    if number in [6, 7]:
        self.swipe(916, 483, 916, 219, duration=0.5, post_sleep_time=0.7)
    if number in [8, 9, 10, 11, 12]:
        self.swipe(943, 698, 943, 0, duration=0.1, post_sleep_time=0.7)
        self.swipe(943, 698, 943, 0, duration=0.1, post_sleep_time=0.7)
    img_possibles = {'activity_menu': (1124, lo[index[number - 1]])}
    img_ends = "normal_task_task-info"
    picture.co_detect(self, None, None, img_ends, img_possibles, True)


def to_challenge_task_info(self, number):
    lo = [0, 178, 279, 377, 477, 564]
    img_possibles = {'activity_menu': (1124, lo[number])}
    img_ends = [
        "normal_task_task-info",
        "normal_task_SUB"
    ]
    return picture.co_detect(self, None, None, img_ends, img_possibles, True)


def to_formation_edit_i(self, i, lo=(0, 0), skip_first_screenshot=False):
    loy = [195, 275, 354, 423]
    y = loy[i - 1]
    rgb_ends = "formation_edit" + str(i)
    rgb_possibles = {
        "formation_edit1": (74, y),
        "formation_edit2": (74, y),
        "formation_edit3": (74, y),
        "formation_edit4": (74, y),
    }
    rgb_possibles.pop("formation_edit" + str(i))
    img_possibles = {
        "normal_task_task-info": (lo[0], lo[1]),
        "normal_task_SUB": (647, 517)
    }
    picture.co_detect(self, rgb_ends, rgb_possibles, None, img_possibles, skip_first_screenshot)


def start_sweep(self, skip_first_screenshot=False):
    img_ends = [
        "purchase_ap_notice",
        "purchase_ap_notice-localized",
        "normal_task_start-sweep-notice",
    ]
    img_possibles = {"normal_task_task-info": (941, 411)}
    res = picture.co_detect(self,None,None, img_ends, img_possibles, skip_first_screenshot)
    if res == "purchase_ap_notice-localized" or res == "purchase_ap_notice":
        return "inadequate_ap"
    rgb_ends = [
        "skip_sweep_complete",
        "sweep_complete"
    ]
    rgb_possibles = {"start_sweep_notice": (765, 501)}
    img_ends = [
        "normal_task_skip-sweep-complete",
        "normal_task_sweep-complete",
    ]
    img_possibles = {"normal_task_start-sweep-notice": (765, 501)}
    picture.co_detect(self, rgb_ends, rgb_possibles, img_ends, img_possibles, skip_first_screenshot)
    return "sweep_complete"


def exchange_reward(self):
    to_activity(self, "story", True)
    to_exchange(self, True)
    to_set_exchange_times_menu(self, True)
    if not image.compare_image(self, "activity_exchange-50-times-at-once"):
        self.logger.info("set exchange times to 50 times at once")
        self.click(778, 320, wait_over=True)
    img_possibles = {"activity_set-exchange-times-menu": (772, 482)}
    img_ends = "activity_exchange-menu"
    picture.co_detect(self, None, None, img_ends, img_possibles, True)
    while 1:
        while color.judge_rgb_range(self, 314, 684, 235, 255, 223, 243, 65, 85):
            self.click(453, 651, wait_over=True, duration = 0.5)
            time.sleep(0.5)
            continue_exchange(self)
            to_exchange(self, True)
        if color.judge_rgb_range(self, 45, 684, 185, 225, 185, 225, 185, 225):
            if get_exchange_assets(self) >= 6:
                self.logger.info("refresh exchange times")
                refresh_exchange_times(self)
                continue
            else:
                self.logger.info("exchange complete")
                return True


def refresh_exchange_times(self):
    img_possibles = {"activity_exchange-menu": (1155, 114)}
    img_ends = "activity_refresh-exchange-times-notice"
    picture.co_detect(self, None, None, img_ends, img_possibles, True)
    img_possibles = {"activity_refresh-exchange-times-notice": (768, 500)}
    img_ends = "activity_exchange-menu"
    picture.co_detect(self, None, None, img_ends, img_possibles, True)


def to_exchange(self, skip_first_screenshot=False):
    img_possibles = {
        "activity_menu": (279, 639),
        "activity_set-exchange-times-menu": (935, 195),
        "activity_exchange-confirm": (673, 603),
    }
    img_ends = "activity_exchange-menu"
    picture.co_detect(self, None, None, img_ends, img_possibles, skip_first_screenshot)


def to_set_exchange_times_menu(self, skip_first_screenshot=False):
    img_possibles = {"activity_exchange-menu": (122, 105)}
    img_ends = "activity_set-exchange-times-menu"
    picture.co_detect(self, None, None, img_ends, img_possibles, skip_first_screenshot)


def continue_exchange(self):
    img_possibles = {"activity_continue-exchange": (931, 600)}
    img_ends = "activity_continue-exchange-grey"
    picture.co_detect(self, None, None, img_ends, img_possibles, True, tentitive_click=True, max_fail_cnt=5)


def get_exchange_assets(self):
    region = {
        "CN": (710, 98, 805, 130),
        "JP": (710, 98, 805, 130),
        "Global": (710, 98, 805, 130),
    }
    return self.ocr.get_region_num(self.latest_img_array, region[self.server], int, self.ratio)


def jointTask(self):
    to_activity(self, "story", True, False)
    toJointTask(self, True)
    tickets = getJointTaskTickets(self)
    if tickets == "UNKNOWN":
        self.logger.warning("joint task tickets: [ UNKNOWN ], assume [ 5, 5 ]")
        tickets = [5, 5]
    self.logger.info("joint task tickets: " + str(tickets))
    for i in range(0, tickets[0]):
        toJointTaskBossInfo(self)
        toJointTaskTaskInfo(self, boss=1)
        self.swipe(378, 403, 375, 493, duration=0.3, post_sleep_time=0.5)
        self.click(375, 490, wait_over=True, duration=0.3)
        startJointFight(self)
        main_story.change_acc_auto(self)
        toJointTask(self)


def toJointTask(self, skip_first_screenshot=False):
    img_possibles = {
        "activity_menu": (103, 229),
        'normal_task_prize-confirm': (776, 655),
        'normal_task_fail-confirm': (643, 658),
        'normal_task_task-finish': (1038, 662),
        'normal_task_fight-confirm': (1168, 659),
        "normal_task_sweep-complete": (643, 585),
        "normal_task_start-sweep-notice": (887, 164),
        'normal_task_skip-sweep-complete': (643, 506),
        'normal_task_fight-complete-confirm': (1160, 666),
        'normal_task_reward-acquired-confirm': (800, 660),
        'normal_task_mission-conclude-confirm': (1042, 671),
    }
    img_ends = "activity_joint-task-menu"
    picture.co_detect(self, None, None, img_ends, img_possibles, skip_first_screenshot)


def toJointTaskBossInfo(self):
    img_possibles = {
        "activity_joint-task-menu": (853, 623),
    }
    img_ends = "activity_joint-task-boss-info"
    picture.co_detect(self, None, None, img_ends, img_possibles, True)


def getJointTaskTickets(self):
    region = {
        "CN": (177, 85, 216,116),
        "JP": (177, 85, 216,116),
        "Global": (177, 85, 216,116),
    }
    try:
        ocr_res = self.ocr.get_region_res(self.latest_img_array, region[self.server], 'Global', self.ratio)
        if ocr_res[1] == '1':
            return [int(ocr_res[0]), int(ocr_res[2])]
        for j in range(0, len(ocr_res)):
            if ocr_res[j] == '/':
                return [int(ocr_res[:j]), int(ocr_res[j + 1:])]
        return "UNKNOWN"
    except Exception as e:
        self.logger.error("getJointTaskTickets error: " + str(e))
        return "UNKNOWN"


def toJointTaskTaskInfo(self, boss=1):
    y = 260
    if boss == 0:
        y = 388
    img_possibles = {
        "activity_joint-task-boss-info": (851, y),
    }
    img_ends = "activity_joint-task-task-info"
    picture.co_detect(self, None, None, img_ends, img_possibles, True)


def startJointFight(self):
    img_possibles = {
        "activity_joint-task-task-info": (1021, 568),
        "activity_joint-task-use-ticket-notice": (759, 500),
    }
    rgb_possibles = {"formation_edit1": (1156, 659)}
    rgb_ends = "fighting_feature"
    picture.co_detect(self, rgb_ends, rgb_possibles, None, img_possibles, True)

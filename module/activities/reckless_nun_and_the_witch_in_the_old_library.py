import importlib
import time
from core import image, color, picture
from module import main_story
from module.explore_normal_task import common_gird_method


def implement(self):
    times = preprocess_activity_sweep_times(self.config["activity_sweep_times"])
    region = preprocess_activity_region(self.config["activity_sweep_task_number"])
    self.logger.info("activity sweep task number : " + str(region))
    self.logger.info("activity sweep times : " + str(times))
    if len(times) > 0:
        return sweep(self, region, times)
    else:
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
    module_path = 'src.explore_task_data.activities.reckless_nun_and_the_witch_in_the_old_library'
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
        click_times = sweep_times
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
    to_activity(self, "story", True)
    last_target_task = 1
    total_stories = 8
    while self.flag_run:
        self.swipe(919, 136, 943, 720, duration=0.05, post_sleep_time=0.5)
        to_story_task_info(self, last_target_task)
        res = color.check_sweep_availability(self)
        while res == "sss" and last_target_task <= total_stories - 1:
            self.logger.info("Current story sss check next story")
            self.click(1168, 353, duration=1, wait_over=True)
            last_target_task += 1
            picture.co_detect(self, img_ends="normal_task_task-info")
            res = color.check_sweep_availability(self)
        if last_target_task == total_stories and res == "sss":
            self.logger.info("All STORY SSS")
            return True
        start_story(self)
        to_activity(self, "mission", True)
        to_activity(self, "story", True)


def start_story(self):
    img_possibles = {
        "normal_task_task-info": (940, 538),
        "plot_menu": (1205, 34),
        "plot_skip-plot-button": (1213, 116),
        "plot_skip-plot-notice": (766, 520),
    }
    rgb_ends = [
        "formation_edit1",
        "reward_acquired",
    ]
    res = picture.co_detect(self, rgb_ends, None, None, img_possibles, skip_first_screenshot=True)
    if res == "formation_edit1":
        start_fight(self, 1)
        main_story.auto_fight(self)
    elif res == "reward_acquired":
        pass
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
        'pierce1',
        'mystic1',
        'burst1',
        'pierce1',
        'pierce1',
        'mystic1',
        'burst1',
        'pierce1',
        'pierce1',
        'mystic1',
        'burst1',
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
        self.logger.info("according to config, choose formation " + str(number))
        to_formation_edit_i(self, number, (940, 538), True)
        start_fight(self, number)
        main_story.auto_fight(self)
        to_activity(self, "story")
        to_activity(self, "mission", True, True)


def explore_challenge(self):
    self.quick_method_to_main_page()
    to_activity(self, "challenge")
    tasks = [
        "challenge2_sss",
        "challenge2_task",
        "challenge4_sss",
        "challenge4_task",
    ]
    stage_data = get_stage_data()
    for i in range(0, len(tasks)):
        current_task_stage_data = stage_data[tasks[i]]
        data = tasks[i].split("_")
        task_number = int(data[0].replace("challenge", ""))
        to_challenge_task_info(self, task_number)
        need_fight = False
        if "task" in data:
            need_fight = True
        elif "sss" in data:
            res = color.check_sweep_availability(self)
            if res == "sss":
                self.logger.info("Challenge " + str(task_number) + " sss no need to fight")
                to_activity(self, "challenge", True)
                continue
            elif res == "no-pass" or res == "pass":
                need_fight = True
        if need_fight:
            common_gird_method(self, current_task_stage_data)
            main_story.auto_fight(self)
            if self.config['manual_boss']:
                self.click(1235, 41)
            to_activity(self, "mission", True)
            to_activity(self, "challenge", True)


def to_activity(self, region, skip_first_screenshot=False, need_swipe=False):
    img_possibles = {
        "activity_enter1": (1196, 195),
        "activity_enter2": (100, 149),
        "activity_enter3": (218, 530),
        'activity_fight-success-confirm': (640, 663),
        "plot_menu": (1205, 34),
        "plot_skip-plot-button": (1213, 116),
        "purchase_ap_notice": (919, 168),
        'purchase_ap_notice-localized': (919, 168),
        "plot_skip-plot-notice": (766, 520),
        "normal_task_help": (1017, 131),
        "normal_task_task-info": (1087, 141),
        "activity_play-guide": (1184, 152),
        'main_story_fight-confirm': (1168, 659),
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
        if not color.judge_rgb_range(self, rgb_lo[region], 121, 20, 60, 40, 70, 70, 100):
            self.click(click_lo[region], 76)
            time.sleep(self.screenshot_interval)
            self.latest_img_array = self.get_screenshot_array()
        else:
            if region == "mission" and need_swipe:
                self.swipe(919, 136, 943, 720, duration=0.05, post_sleep_time=0.5)
                self.swipe(919, 136, 943, 720, duration=0.05, post_sleep_time=0.5)
            return True


def to_story_task_info(self, number):
    lo = [0, 184, 277, 375, 480, 574]
    index = [0, 1, 2, 3, 4, 5, 3, 4, 5]
    if number in [6, 7, 8, 9, 10]:
        self.swipe(943, 593, 943, 0, duration=0.1, post_sleep_time=0.7)
    img_possibles = {'activity_menu': (1124, lo[index[number]])}
    img_ends = "normal_task_task-info"
    picture.co_detect(self, None, None, img_ends, img_possibles, True)


def to_mission_task_info(self, number):
    lo = [0, 184, 300, 416, 527]
    index = [0, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
    if number >= 5:
        self.swipe(943, 593, 943, 102, duration=0.5, post_sleep_time=0.7)
    if number >= 9:
        self.swipe(943, 593, 943, 102, duration=0.5, post_sleep_time=0.7)
    img_possibles = {'activity_menu': (1124, lo[index[number]])}
    img_ends = "normal_task_task-info"
    picture.co_detect(self, None, None, img_ends, img_possibles, True)


def to_challenge_task_info(self, number):
    lo = [0, 178, 279, 377, 477, 564]
    img_possibles = {'activity_menu': (1124, lo[number])}
    img_ends = "normal_task_task-info"
    picture.co_detect(self, None, None, img_ends, img_possibles, True)





def to_formation_edit_i(self, i, lo, skip_first_screenshot=False):
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
    img_possibles = {"normal_task_task-info": (lo[0], lo[1])}
    picture.co_detect(self, rgb_ends, rgb_possibles, None, img_possibles, skip_first_screenshot)


def start_sweep(self, skip_first_screenshot=False):
    img_ends = [
        "purchase_ap_notice",
        "purchase_ap_notice-localized",
        "normal_task_start-sweep-notice",
    ]
    img_possibles = {"normal_task_task-info": (941, 411)}
    res = picture.co_detect(self, None, None, img_ends, img_possibles, skip_first_screenshot)
    if res == "purchase_ap_notice-localized" or res == "buy_ap_notice":
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


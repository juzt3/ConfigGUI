import os

import dearpygui.dearpygui as dpg
from dearpygui_ext.themes import create_theme_imgui_dark

from SettingsHandler import *

dpg.create_context()
dpg.create_viewport(title="Config Manager", width=416, height=272)
settings = get_settings()

h_types_selected = settings['hTypes']

wood_tiers = settings['woodTiers']
ore_tiers = settings['oreTiers']
hide_tiers = settings['hideTiers']
fiber_tiers = settings['fiberTiers']
rock_tiers = settings['rockTiers']

wood_mob_tiers = settings['woodMobsTiers']
ore_mob_tiers = settings['oreMobsTiers']
hide_mob_tiers = settings['hideMobsTiers']
fiber_mob_tiers = settings['fiberMobsTiers']
rock_mob_tiers = settings['rockMobsTiers']


def h_types_callback(sender, app_data):
    if dpg.get_value(sender):  # Checkbox activado
        if "wood" in sender:
            h_types_selected.append('WOOD')
            dpg.configure_item("tab_wood", show=True)
            dpg.configure_item("tab_wood_mobs", show=True)
        elif "fiber" in sender:
            h_types_selected.append('FIBER')
            dpg.configure_item("tab_fiber", show=True)
            dpg.configure_item("tab_fiber_mobs", show=True)
        elif "ore" in sender:
            h_types_selected.append('ORE')
            dpg.configure_item("tab_ore", show=True)
            dpg.configure_item("tab_ore_mobs", show=True)
        elif "rock" in sender:
            h_types_selected.append('ROCK')
            dpg.configure_item("tab_rock", show=True)
            dpg.configure_item("tab_rock_mobs", show=True)
        elif "hide" in sender:
            h_types_selected.append('HIDE')
            dpg.configure_item("tab_hide", show=True)
            dpg.configure_item("tab_hide_mobs", show=True)
    else:  # Checkbox desactivado
        if "wood" in sender:
            h_types_selected.remove("WOOD")
            dpg.configure_item("tab_wood", show=False)
            dpg.configure_item("tab_wood_mobs", show=False)
        elif "fiber" in sender:
            h_types_selected.remove("FIBER")
            dpg.configure_item("tab_fiber", show=False)
            dpg.configure_item("tab_fiber_mobs", show=False)
        elif "ore" in sender:
            h_types_selected.remove("ORE")
            dpg.configure_item("tab_ore", show=False)
            dpg.configure_item("tab_ore_mobs", show=False)
        elif "rock" in sender:
            h_types_selected.remove("ROCK")
            dpg.configure_item("tab_rock", show=False)
            dpg.configure_item("tab_rock_mobs", show=False)
        elif "hide" in sender:
            h_types_selected.remove("HIDE")
            dpg.configure_item("tab_hide", show=False)
            dpg.configure_item("tab_hide_mobs", show=False)


def h_tier_callback(sender, add_data):
    label = float(dpg.get_item_label(sender))

    if dpg.get_value(sender):  # Checkbox activado
        if "wood" in sender:
            wood_tiers.append(label)
        elif "fiber" in sender:
            fiber_tiers.append(label)
        elif "ore" in sender:
            ore_tiers.append(label)
        elif "rock" in sender:
            rock_tiers.append(label)
        elif "hide" in sender:
            hide_tiers.append(label)
    else:  # Checkbox desactivado
        if "wood" in sender:
            wood_tiers.remove(label)
        elif "fiber" in sender:
            fiber_tiers.remove(label)
        elif "ore" in sender:
            ore_tiers.remove(label)
        elif "rock" in sender:
            rock_tiers.remove(label)
        elif "hide" in sender:
            hide_tiers.remove(label)


def h_mobs_tier_callback(sender, add_data):
    label = float(dpg.get_item_label(sender))

    if dpg.get_value(sender):  # Checkbox activado
        if "wood" in sender:
            wood_mob_tiers.append(label)
        elif "fiber" in sender:
            fiber_mob_tiers.append(label)
        elif "ore" in sender:
            ore_mob_tiers.append(label)
        elif "rock" in sender:
            rock_mob_tiers.append(label)
        elif "hide" in sender:
            hide_mob_tiers.append(label)
    else:  # Checkbox desactivado
        if "wood" in sender:
            wood_mob_tiers.remove(label)
        elif "fiber" in sender:
            fiber_mob_tiers.remove(label)
        elif "ore" in sender:
            ore_mob_tiers.remove(label)
        elif "rock" in sender:
            rock_mob_tiers.remove(label)
        elif "hide" in sender:
            hide_mob_tiers.remove(label)


def save_settings_callback():
    settings['mainCityId'] = dpg.get_value('city_id')
    settings['gatheringMapId'] = dpg.get_value('gathering_map_id')
    settings['safeZone'] = dpg.get_value('safe_zone_checkbox')
    settings['dilation'] = dpg.get_value('map_dilation')

    settings['lowHealth'] = dpg.get_value('low_health')
    settings['q_skill_cooldown'] = dpg.get_value('q_cooldown')
    settings['q_skill_max_uses'] = dpg.get_value('q_max_uses')
    settings['q_skill_channel_time'] = dpg.get_value('q_channeling')
    settings['q_skill_must_target'] = dpg.get_value('q_must_target')

    settings['w_skill_cooldown'] = dpg.get_value('w_cooldown')
    settings['w_skill_max_uses'] = dpg.get_value('w_max_uses')
    settings['w_skill_channel_time'] = dpg.get_value('w_channeling')
    settings['w_skill_must_target'] = dpg.get_value('w_must_target')

    settings['e_skill_cooldown'] = dpg.get_value('e_cooldown')
    settings['e_skill_max_uses'] = dpg.get_value('e_max_uses')
    settings['e_skill_channel_time'] = dpg.get_value('e_channeling')
    settings['e_skill_must_target'] = dpg.get_value('e_must_target')

    settings['r_skill_cooldown'] = dpg.get_value('r_cooldown')
    settings['r_skill_max_uses'] = dpg.get_value('r_max_uses')
    settings['r_skill_channel_time'] = dpg.get_value('r_channeling')
    settings['r_skill_must_target'] = dpg.get_value('r_must_target')

    settings['oreTiers'] = ore_tiers
    settings['hideTiers'] = hide_tiers
    settings['fiberTiers'] = fiber_tiers
    settings['rockTiers'] = rock_tiers
    settings['woodTiers'] = wood_tiers

    settings['minCharges'] = dpg.get_value('min_charges')

    settings['oreMobsTiers'] = ore_mob_tiers
    settings['hideMobsTiers'] = hide_mob_tiers
    settings['fiberMobsTiers'] = fiber_mob_tiers
    settings['rockMobsTiers'] = rock_mob_tiers
    settings['woodMobsTiers'] = wood_mob_tiers

    settings['API_SERVER'] = dpg.get_value('api_ip')
    settings['API_KEY'] = dpg.get_value('api_key')
    settings['CHAT_ID'] = dpg.get_value('chat_id')
    settings['BOT_NAME'] = dpg.get_value('bot_name')

    save_settings(settings)
    return


with dpg.window(tag="main_window", no_close=True, no_resize=True, no_move=True):
    with dpg.window(tag="settings_window", label="Settings", width=400, height=232, pos=[0, 0], no_resize=True, no_close=True, no_move=True, no_collapse=True):
        with dpg.tab_bar(tag="tab_bar"):
            with dpg.tab(tag="tab_settings", label="Settings"):
                with dpg.table(tag="tbl_settings", height=150, scrollY=True, header_row=False):
                    dpg.add_table_column(tag="settings_text", width_fixed=True)
                    dpg.add_table_column(tag="settings_input", width_stretch=True)

                    with dpg.table_row(label="Map Settings"):
                        dpg.add_text("City ID: ")
                        dpg.add_input_text(tag="city_id", default_value=settings['mainCityId'])
                    with dpg.table_row():
                        dpg.add_text("Gathering Map ID: ")
                        dpg.add_input_text(tag="gathering_map_id", default_value=settings['gatheringMapId'])
                    with dpg.table_row():
                        dpg.add_text("Safe Zone: ")
                        dpg.add_checkbox(tag="safe_zone_checkbox", default_value=settings['safeZone'])
                    with dpg.table_row():
                        dpg.add_text("Map Dilation: ")
                        dpg.add_input_int(tag="map_dilation", default_value=settings['dilation'], min_clamped=True, max_clamped=True)

                dpg.add_button(label="Save", callback=save_settings_callback)

            with dpg.tab(tag="tab_gathering", label="Gathering"):
                dpg.add_text("Harvestables")
                with dpg.group(horizontal=True):
                    dpg.add_text("Minimum Charges: ")
                    dpg.add_input_int(tag="min_charges", min_clamped=True, max_clamped=True, min_value=1, max_value=30, default_value=settings['minCharges'])

                with dpg.group(horizontal=True):
                    dpg.add_checkbox(label="Wood", tag="wood_check", default_value=bool("WOOD" in settings['hTypes']), callback=h_types_callback)
                    dpg.add_checkbox(label="Rock", tag="rock_check", default_value=bool("ROCK" in settings['hTypes']), callback=h_types_callback)
                    dpg.add_checkbox(label="Ore", tag="ore_check", default_value=bool("ORE" in settings['hTypes']), callback=h_types_callback)
                    dpg.add_checkbox(label="Hide", tag="hide_check", default_value=bool("HIDE" in settings['hTypes']), callback=h_types_callback)
                    dpg.add_checkbox(label="Fiber", tag="fiber_check", default_value=bool("FIBER" in settings['hTypes']), callback=h_types_callback)

                with dpg.tab_bar(tag="tab_h_tiers"):
                    with dpg.tab(tag="tab_wood", label="Wood", show=bool("WOOD" in settings['hTypes'])):
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="1", tag="wood_1_check", callback=h_tier_callback, default_value=bool(1 in wood_tiers))
                            dpg.add_checkbox(label="2", tag="wood_2_check", callback=h_tier_callback, default_value=bool(2 in wood_tiers))
                            dpg.add_checkbox(label="3", tag="wood_3_check", callback=h_tier_callback, default_value=bool(3 in wood_tiers))
                            dpg.add_checkbox(label="4", tag="wood_4_check", callback=h_tier_callback, default_value=bool(4 in wood_tiers))
                            dpg.add_checkbox(label="4.1", tag="wood_41_check", callback=h_tier_callback, default_value=bool(4.1 in wood_tiers))
                            dpg.add_checkbox(label="4.2", tag="wood_42_check", callback=h_tier_callback, default_value=bool(4.2 in wood_tiers))
                            dpg.add_checkbox(label="4.3", tag="wood_43_check", callback=h_tier_callback, default_value=bool(4.3 in wood_tiers))
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="5", tag="wood_5_check", callback=h_tier_callback, default_value=bool(5 in wood_tiers))
                            dpg.add_checkbox(label="5.1", tag="wood_51_check", callback=h_tier_callback, default_value=bool(5.1 in wood_tiers))
                            dpg.add_checkbox(label="5.2", tag="wood_52_check", callback=h_tier_callback, default_value=bool(5.2 in wood_tiers))
                            dpg.add_checkbox(label="5.3", tag="wood_53_check", callback=h_tier_callback, default_value=bool(5.3 in wood_tiers))
                            dpg.add_checkbox(label="6", tag="wood_6_check", callback=h_tier_callback, default_value=bool(6 in wood_tiers))
                            dpg.add_checkbox(label="6.1", tag="wood_61_check", callback=h_tier_callback, default_value=bool(6.1 in wood_tiers))
                            dpg.add_checkbox(label="6.2", tag="wood_62_check", callback=h_tier_callback, default_value=bool(6.2 in wood_tiers))
                            dpg.add_checkbox(label="6.3", tag="wood_63_check", callback=h_tier_callback, default_value=bool(6.3 in wood_tiers))
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="7", tag="wood_7_check", callback=h_tier_callback, default_value=bool(7 in wood_tiers))
                            dpg.add_checkbox(label="7.1", tag="wood_71_check", callback=h_tier_callback, default_value=bool(7.1 in wood_tiers))
                            dpg.add_checkbox(label="7.2", tag="wood_72_check", callback=h_tier_callback, default_value=bool(7.2 in wood_tiers))
                            dpg.add_checkbox(label="7.3", tag="wood_73_check", callback=h_tier_callback, default_value=bool(7.3 in wood_tiers))
                            dpg.add_checkbox(label="8", tag="wood_8_check", callback=h_tier_callback, default_value=bool(8 in wood_tiers))
                            dpg.add_checkbox(label="8.1", tag="wood_81_check", callback=h_tier_callback, default_value=bool(8.1 in wood_tiers))
                            dpg.add_checkbox(label="8.2", tag="wood_82_check", callback=h_tier_callback, default_value=bool(8.2 in wood_tiers))
                            dpg.add_checkbox(label="8.3", tag="wood_83_check", callback=h_tier_callback, default_value=bool(8.3 in wood_tiers))

                    with dpg.tab(tag="tab_rock", label="Rock", show=bool("ROCK" in settings['hTypes'])):
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="1", tag="rock_1_check", callback=h_tier_callback, default_value=bool(1 in rock_tiers))
                            dpg.add_checkbox(label="2", tag="rock_2_check", callback=h_tier_callback, default_value=bool(2 in rock_tiers))
                            dpg.add_checkbox(label="3", tag="rock_3_check", callback=h_tier_callback, default_value=bool(3 in rock_tiers))
                            dpg.add_checkbox(label="4", tag="rock_4_check", callback=h_tier_callback, default_value=bool(4 in rock_tiers))
                            dpg.add_checkbox(label="4.1", tag="rock_41_check", callback=h_tier_callback, default_value=bool(4.1 in rock_tiers))
                            dpg.add_checkbox(label="4.2", tag="rock_42_check", callback=h_tier_callback, default_value=bool(4.2 in rock_tiers))
                            dpg.add_checkbox(label="4.3", tag="rock_43_check", callback=h_tier_callback, default_value=bool(4.3 in rock_tiers))
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="5", tag="rock_5_check", callback=h_tier_callback, default_value=bool(5 in rock_tiers))
                            dpg.add_checkbox(label="5.1", tag="rock_51_check", callback=h_tier_callback, default_value=bool(5.1 in rock_tiers))
                            dpg.add_checkbox(label="5.2", tag="rock_52_check", callback=h_tier_callback, default_value=bool(5.2 in rock_tiers))
                            dpg.add_checkbox(label="5.3", tag="rock_53_check", callback=h_tier_callback, default_value=bool(5.3 in rock_tiers))
                            dpg.add_checkbox(label="6", tag="rock_6_check", callback=h_tier_callback, default_value=bool(6 in rock_tiers))
                            dpg.add_checkbox(label="6.1", tag="rock_61_check", callback=h_tier_callback, default_value=bool(6.1 in rock_tiers))
                            dpg.add_checkbox(label="6.2", tag="rock_62_check", callback=h_tier_callback, default_value=bool(6.2 in rock_tiers))
                            dpg.add_checkbox(label="6.3", tag="rock_63_check", callback=h_tier_callback, default_value=bool(6.3 in rock_tiers))
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="7", tag="rock_7_check", callback=h_tier_callback, default_value=bool(7 in rock_tiers))
                            dpg.add_checkbox(label="7.1", tag="rock_71_check", callback=h_tier_callback, default_value=bool(7.1 in rock_tiers))
                            dpg.add_checkbox(label="7.2", tag="rock_72_check", callback=h_tier_callback, default_value=bool(7.2 in rock_tiers))
                            dpg.add_checkbox(label="7.3", tag="rock_73_check", callback=h_tier_callback, default_value=bool(7.3 in rock_tiers))
                            dpg.add_checkbox(label="8", tag="rock_8_check", callback=h_tier_callback, default_value=bool(8 in rock_tiers))
                            dpg.add_checkbox(label="8.1", tag="rock_81_check", callback=h_tier_callback, default_value=bool(8.1 in rock_tiers))
                            dpg.add_checkbox(label="8.2", tag="rock_82_check", callback=h_tier_callback, default_value=bool(8.2 in rock_tiers))
                            dpg.add_checkbox(label="8.3", tag="rock_83_check", callback=h_tier_callback, default_value=bool(8.3 in rock_tiers))

                    with dpg.tab(tag="tab_ore", label="Ore", show=bool("ORE" in settings['hTypes'])):
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="1", tag="ore_1_check", callback=h_tier_callback, default_value=bool(1 in ore_tiers))
                            dpg.add_checkbox(label="2", tag="ore_2_check", callback=h_tier_callback, default_value=bool(2 in ore_tiers))
                            dpg.add_checkbox(label="3", tag="ore_3_check", callback=h_tier_callback, default_value=bool(3 in ore_tiers))
                            dpg.add_checkbox(label="4", tag="ore_4_check", callback=h_tier_callback, default_value=bool(4 in ore_tiers))
                            dpg.add_checkbox(label="4.1", tag="ore_41_check", callback=h_tier_callback, default_value=bool(4.1 in ore_tiers))
                            dpg.add_checkbox(label="4.2", tag="ore_42_check", callback=h_tier_callback, default_value=bool(4.2 in ore_tiers))
                            dpg.add_checkbox(label="4.3", tag="ore_43_check", callback=h_tier_callback, default_value=bool(4.3 in ore_tiers))
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="5", tag="ore_5_check", callback=h_tier_callback, default_value=bool(5 in ore_tiers))
                            dpg.add_checkbox(label="5.1", tag="ore_51_check", callback=h_tier_callback, default_value=bool(5.1 in ore_tiers))
                            dpg.add_checkbox(label="5.2", tag="ore_52_check", callback=h_tier_callback, default_value=bool(5.2 in ore_tiers))
                            dpg.add_checkbox(label="5.3", tag="ore_53_check", callback=h_tier_callback, default_value=bool(5.3 in ore_tiers))
                            dpg.add_checkbox(label="6", tag="ore_6_check", callback=h_tier_callback, default_value=bool(6 in ore_tiers))
                            dpg.add_checkbox(label="6.1", tag="ore_61_check", callback=h_tier_callback, default_value=bool(6.1 in ore_tiers))
                            dpg.add_checkbox(label="6.2", tag="ore_62_check", callback=h_tier_callback, default_value=bool(6.2 in ore_tiers))
                            dpg.add_checkbox(label="6.3", tag="ore_63_check", callback=h_tier_callback, default_value=bool(6.3 in ore_tiers))
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="7", tag="ore_7_check", callback=h_tier_callback, default_value=bool(7 in ore_tiers))
                            dpg.add_checkbox(label="7.1", tag="ore_71_check", callback=h_tier_callback, default_value=bool(7.1 in ore_tiers))
                            dpg.add_checkbox(label="7.2", tag="ore_72_check", callback=h_tier_callback, default_value=bool(7.2 in ore_tiers))
                            dpg.add_checkbox(label="7.3", tag="ore_73_check", callback=h_tier_callback, default_value=bool(7.3 in ore_tiers))
                            dpg.add_checkbox(label="8", tag="ore_8_check", callback=h_tier_callback, default_value=bool(8 in ore_tiers))
                            dpg.add_checkbox(label="8.1", tag="ore_81_check", callback=h_tier_callback, default_value=bool(8.1 in ore_tiers))
                            dpg.add_checkbox(label="8.2", tag="ore_82_check", callback=h_tier_callback, default_value=bool(8.2 in ore_tiers))
                            dpg.add_checkbox(label="8.3", tag="ore_83_check", callback=h_tier_callback, default_value=bool(8.3 in ore_tiers))

                    with dpg.tab(tag="tab_hide", label="Hide", show=bool("HIDE" in settings['hTypes'])):
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="1", tag="hide_1_check", callback=h_tier_callback, default_value=bool(1 in hide_tiers))
                            dpg.add_checkbox(label="2", tag="hide_2_check", callback=h_tier_callback, default_value=bool(2 in hide_tiers))
                            dpg.add_checkbox(label="3", tag="hide_3_check", callback=h_tier_callback, default_value=bool(3 in hide_tiers))
                            dpg.add_checkbox(label="4", tag="hide_4_check", callback=h_tier_callback, default_value=bool(4 in hide_tiers))
                            dpg.add_checkbox(label="4.1", tag="hide_41_check", callback=h_tier_callback, default_value=bool(4.1 in hide_tiers))
                            dpg.add_checkbox(label="4.2", tag="hide_42_check", callback=h_tier_callback, default_value=bool(4.2 in hide_tiers))
                            dpg.add_checkbox(label="4.3", tag="hide_43_check", callback=h_tier_callback, default_value=bool(4.3 in hide_tiers))
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="5", tag="hide_5_check", callback=h_tier_callback, default_value=bool(5 in hide_tiers))
                            dpg.add_checkbox(label="5.1", tag="hide_51_check", callback=h_tier_callback, default_value=bool(5.1 in hide_tiers))
                            dpg.add_checkbox(label="5.2", tag="hide_52_check", callback=h_tier_callback, default_value=bool(5.2 in hide_tiers))
                            dpg.add_checkbox(label="5.3", tag="hide_53_check", callback=h_tier_callback, default_value=bool(5.3 in hide_tiers))
                            dpg.add_checkbox(label="6", tag="hide_6_check", callback=h_tier_callback, default_value=bool(6 in hide_tiers))
                            dpg.add_checkbox(label="6.1", tag="hide_61_check", callback=h_tier_callback, default_value=bool(6.1 in hide_tiers))
                            dpg.add_checkbox(label="6.2", tag="hide_62_check", callback=h_tier_callback, default_value=bool(6.2 in hide_tiers))
                            dpg.add_checkbox(label="6.3", tag="hide_63_check", callback=h_tier_callback, default_value=bool(6.3 in hide_tiers))
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="7", tag="hide_7_check", callback=h_tier_callback, default_value=bool(7 in hide_tiers))
                            dpg.add_checkbox(label="7.1", tag="hide_71_check", callback=h_tier_callback, default_value=bool(7.1 in hide_tiers))
                            dpg.add_checkbox(label="7.2", tag="hide_72_check", callback=h_tier_callback, default_value=bool(7.2 in hide_tiers))
                            dpg.add_checkbox(label="7.3", tag="hide_73_check", callback=h_tier_callback, default_value=bool(7.3 in hide_tiers))
                            dpg.add_checkbox(label="8", tag="hide_8_check", callback=h_tier_callback, default_value=bool(8 in hide_tiers))
                            dpg.add_checkbox(label="8.1", tag="hide_81_check", callback=h_tier_callback, default_value=bool(8.1 in hide_tiers))
                            dpg.add_checkbox(label="8.2", tag="hide_82_check", callback=h_tier_callback, default_value=bool(8.2 in hide_tiers))
                            dpg.add_checkbox(label="8.3", tag="hide_83_check", callback=h_tier_callback, default_value=bool(8.3 in hide_tiers))

                    with dpg.tab(tag="tab_fiber", label="Fiber", show=bool("FIBER" in settings['hTypes'])):
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="1", tag="fiber_1_check", callback=h_tier_callback, default_value=bool(1 in fiber_tiers))
                            dpg.add_checkbox(label="2", tag="fiber_2_check", callback=h_tier_callback, default_value=bool(2 in fiber_tiers))
                            dpg.add_checkbox(label="3", tag="fiber_3_check", callback=h_tier_callback, default_value=bool(3 in fiber_tiers))
                            dpg.add_checkbox(label="4", tag="fiber_4_check", callback=h_tier_callback, default_value=bool(4 in fiber_tiers))
                            dpg.add_checkbox(label="4.1", tag="fiber_41_check", callback=h_tier_callback, default_value=bool(4.1 in fiber_tiers))
                            dpg.add_checkbox(label="4.2", tag="fiber_42_check", callback=h_tier_callback, default_value=bool(4.2 in fiber_tiers))
                            dpg.add_checkbox(label="4.3", tag="fiber_43_check", callback=h_tier_callback, default_value=bool(4.3 in fiber_tiers))
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="5", tag="fiber_5_check", callback=h_tier_callback, default_value=bool(5 in fiber_tiers))
                            dpg.add_checkbox(label="5.1", tag="fiber_51_check", callback=h_tier_callback, default_value=bool(5.1 in fiber_tiers))
                            dpg.add_checkbox(label="5.2", tag="fiber_52_check", callback=h_tier_callback, default_value=bool(5.2 in fiber_tiers))
                            dpg.add_checkbox(label="5.3", tag="fiber_53_check", callback=h_tier_callback, default_value=bool(5.3 in fiber_tiers))
                            dpg.add_checkbox(label="6", tag="fiber_6_check", callback=h_tier_callback, default_value=bool(6 in fiber_tiers))
                            dpg.add_checkbox(label="6.1", tag="fiber_61_check", callback=h_tier_callback, default_value=bool(6.1 in fiber_tiers))
                            dpg.add_checkbox(label="6.2", tag="fiber_62_check", callback=h_tier_callback, default_value=bool(6.2 in fiber_tiers))
                            dpg.add_checkbox(label="6.3", tag="fiber_63_check", callback=h_tier_callback, default_value=bool(6.3 in fiber_tiers))
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="7", tag="fiber_7_check", callback=h_tier_callback, default_value=bool(7 in fiber_tiers))
                            dpg.add_checkbox(label="7.1", tag="fiber_71_check", callback=h_tier_callback, default_value=bool(7.1 in fiber_tiers))
                            dpg.add_checkbox(label="7.2", tag="fiber_72_check", callback=h_tier_callback, default_value=bool(7.2 in fiber_tiers))
                            dpg.add_checkbox(label="7.3", tag="fiber_73_check", callback=h_tier_callback, default_value=bool(7.3 in fiber_tiers))
                            dpg.add_checkbox(label="8", tag="fiber_8_check", callback=h_tier_callback, default_value=bool(8 in fiber_tiers))
                            dpg.add_checkbox(label="8.1", tag="fiber_81_check", callback=h_tier_callback, default_value=bool(8.1 in fiber_tiers))
                            dpg.add_checkbox(label="8.2", tag="fiber_82_check", callback=h_tier_callback, default_value=bool(8.2 in fiber_tiers))
                            dpg.add_checkbox(label="8.3", tag="fiber_83_check", callback=h_tier_callback, default_value=bool(8.3 in fiber_tiers))

            with dpg.tab(tag="tab_mobs", label="Mobs"):
                dpg.add_text("Mobs Tiers")
                with dpg.tab_bar(tag="tab_mobs_tiers"):
                    with dpg.tab(tag="tab_wood_mobs", label="Wood", show=bool("WOOD" in settings['hTypes'])):
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="1", tag="wood_mobs_1_check", callback=h_mobs_tier_callback,
                                             default_value=bool(1 in wood_mob_tiers))
                            dpg.add_checkbox(label="2", tag="wood_mobs_2_check", callback=h_mobs_tier_callback,
                                             default_value=bool(2 in wood_mob_tiers))
                            dpg.add_checkbox(label="3", tag="wood_mobs_3_check", callback=h_mobs_tier_callback,
                                             default_value=bool(3 in wood_mob_tiers))
                            dpg.add_checkbox(label="4", tag="wood_mobs_4_check", callback=h_mobs_tier_callback,
                                             default_value=bool(4 in wood_mob_tiers))
                            dpg.add_checkbox(label="4.1", tag="wood_mobs_41_check", callback=h_mobs_tier_callback,
                                             default_value=bool(4.1 in wood_mob_tiers))
                            dpg.add_checkbox(label="4.2", tag="wood_mobs_42_check", callback=h_mobs_tier_callback,
                                             default_value=bool(4.2 in wood_mob_tiers))
                            dpg.add_checkbox(label="4.3", tag="wood_mobs_43_check", callback=h_mobs_tier_callback,
                                             default_value=bool(4.3 in wood_mob_tiers))
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="5", tag="wood_mobs_5_check", callback=h_mobs_tier_callback,
                                             default_value=bool(5 in wood_mob_tiers))
                            dpg.add_checkbox(label="5.1", tag="wood_mobs_51_check", callback=h_mobs_tier_callback,
                                             default_value=bool(5.1 in wood_mob_tiers))
                            dpg.add_checkbox(label="5.2", tag="wood_mobs_52_check", callback=h_mobs_tier_callback,
                                             default_value=bool(5.2 in wood_mob_tiers))
                            dpg.add_checkbox(label="5.3", tag="wood_mobs_53_check", callback=h_mobs_tier_callback,
                                             default_value=bool(5.3 in wood_mob_tiers))
                            dpg.add_checkbox(label="6", tag="wood_mobs_6_check", callback=h_mobs_tier_callback,
                                             default_value=bool(6 in wood_mob_tiers))
                            dpg.add_checkbox(label="6.1", tag="wood_mobs_61_check", callback=h_mobs_tier_callback,
                                             default_value=bool(6.1 in wood_mob_tiers))
                            dpg.add_checkbox(label="6.2", tag="wood_mobs_62_check", callback=h_mobs_tier_callback,
                                             default_value=bool(6.2 in wood_mob_tiers))
                            dpg.add_checkbox(label="6.3", tag="wood_mobs_63_check", callback=h_mobs_tier_callback,
                                             default_value=bool(6.3 in wood_mob_tiers))
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="7", tag="wood_mobs_7_check", callback=h_mobs_tier_callback,
                                             default_value=bool(7 in wood_mob_tiers))
                            dpg.add_checkbox(label="7.1", tag="wood_mobs_71_check", callback=h_mobs_tier_callback,
                                             default_value=bool(7.1 in wood_mob_tiers))
                            dpg.add_checkbox(label="7.2", tag="woo_mobs_72_check", callback=h_mobs_tier_callback,
                                             default_value=bool(7.2 in wood_mob_tiers))
                            dpg.add_checkbox(label="7.3", tag="wood_mobs_73_check", callback=h_mobs_tier_callback,
                                             default_value=bool(7.3 in wood_mob_tiers))
                            dpg.add_checkbox(label="8", tag="wood_mobs_8_check", callback=h_mobs_tier_callback,
                                             default_value=bool(8 in wood_mob_tiers))
                            dpg.add_checkbox(label="8.1", tag="wood_mobs_81_check", callback=h_mobs_tier_callback,
                                             default_value=bool(8.1 in wood_mob_tiers))
                            dpg.add_checkbox(label="8.2", tag="wood_mobs_82_check", callback=h_mobs_tier_callback,
                                             default_value=bool(8.2 in wood_mob_tiers))
                            dpg.add_checkbox(label="8.3", tag="wood_mobs_83_check", callback=h_mobs_tier_callback,
                                             default_value=bool(8.3 in wood_mob_tiers))

                    with dpg.tab(tag="tab_rock_mobs", label="Rock", show=bool("ROCK" in settings['hTypes'])):
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="1", tag="rock_mobs_1_check", callback=h_mobs_tier_callback,
                                             default_value=bool(1 in rock_mob_tiers))
                            dpg.add_checkbox(label="2", tag="rock_mobs_2_check", callback=h_mobs_tier_callback,
                                             default_value=bool(2 in rock_mob_tiers))
                            dpg.add_checkbox(label="3", tag="rock_mobs_3_check", callback=h_mobs_tier_callback,
                                             default_value=bool(3 in rock_mob_tiers))
                            dpg.add_checkbox(label="4", tag="rock_mobs_4_check", callback=h_mobs_tier_callback,
                                             default_value=bool(4 in rock_mob_tiers))
                            dpg.add_checkbox(label="4.1", tag="rock_mobs_41_check", callback=h_mobs_tier_callback,
                                             default_value=bool(4.1 in rock_mob_tiers))
                            dpg.add_checkbox(label="4.2", tag="rock_mobs_42_check", callback=h_mobs_tier_callback,
                                             default_value=bool(4.2 in rock_mob_tiers))
                            dpg.add_checkbox(label="4.3", tag="rock_mobs_43_check", callback=h_mobs_tier_callback,
                                             default_value=bool(4.3 in rock_mob_tiers))
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="5", tag="rock_mobs_5_check", callback=h_mobs_tier_callback,
                                             default_value=bool(5 in rock_mob_tiers))
                            dpg.add_checkbox(label="5.1", tag="rock_mobs_51_check", callback=h_mobs_tier_callback,
                                             default_value=bool(5.1 in rock_mob_tiers))
                            dpg.add_checkbox(label="5.2", tag="rock_mobs_52_check", callback=h_mobs_tier_callback,
                                             default_value=bool(5.2 in rock_mob_tiers))
                            dpg.add_checkbox(label="5.3", tag="rock_mobs_53_check", callback=h_mobs_tier_callback,
                                             default_value=bool(5.3 in rock_mob_tiers))
                            dpg.add_checkbox(label="6", tag="rock_mobs_6_check", callback=h_mobs_tier_callback,
                                             default_value=bool(6 in rock_mob_tiers))
                            dpg.add_checkbox(label="6.1", tag="rock_mobs_61_check", callback=h_mobs_tier_callback,
                                             default_value=bool(6.1 in rock_mob_tiers))
                            dpg.add_checkbox(label="6.2", tag="rock_mobs_62_check", callback=h_mobs_tier_callback,
                                             default_value=bool(6.2 in rock_mob_tiers))
                            dpg.add_checkbox(label="6.3", tag="rock_mobs_63_check", callback=h_mobs_tier_callback,
                                             default_value=bool(6.3 in rock_mob_tiers))
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="7", tag="rock_mobs_7_check", callback=h_mobs_tier_callback,
                                             default_value=bool(7 in rock_mob_tiers))
                            dpg.add_checkbox(label="7.1", tag="rock_mobs_71_check", callback=h_mobs_tier_callback,
                                             default_value=bool(7.1 in rock_mob_tiers))
                            dpg.add_checkbox(label="7.2", tag="rock_mobs_72_check", callback=h_mobs_tier_callback,
                                             default_value=bool(7.2 in rock_mob_tiers))
                            dpg.add_checkbox(label="7.3", tag="rock_mobs_73_check", callback=h_mobs_tier_callback,
                                             default_value=bool(7.3 in rock_mob_tiers))
                            dpg.add_checkbox(label="8", tag="rock_mobs_8_check", callback=h_mobs_tier_callback,
                                             default_value=bool(8 in rock_mob_tiers))
                            dpg.add_checkbox(label="8.1", tag="rock_mobs_81_check", callback=h_mobs_tier_callback,
                                             default_value=bool(8.1 in rock_mob_tiers))
                            dpg.add_checkbox(label="8.2", tag="rock_mobs_82_check", callback=h_mobs_tier_callback,
                                             default_value=bool(8.2 in rock_mob_tiers))
                            dpg.add_checkbox(label="8.3", tag="rock_mobs_83_check", callback=h_mobs_tier_callback,
                                             default_value=bool(8.3 in rock_mob_tiers))

                    with dpg.tab(tag="tab_ore_mobs", label="Ore", show=bool("ORE" in settings['hTypes'])):
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="1", tag="ore_mobs_1_check", callback=h_mobs_tier_callback,
                                             default_value=bool(1 in ore_mob_tiers))
                            dpg.add_checkbox(label="2", tag="ore_mobs_2_check", callback=h_mobs_tier_callback,
                                             default_value=bool(2 in ore_mob_tiers))
                            dpg.add_checkbox(label="3", tag="ore_mobs_3_check", callback=h_mobs_tier_callback,
                                             default_value=bool(3 in ore_mob_tiers))
                            dpg.add_checkbox(label="4", tag="ore_mobs_4_check", callback=h_mobs_tier_callback,
                                             default_value=bool(4 in ore_mob_tiers))
                            dpg.add_checkbox(label="4.1", tag="ore_mobs_41_check", callback=h_mobs_tier_callback,
                                             default_value=bool(4.1 in ore_mob_tiers))
                            dpg.add_checkbox(label="4.2", tag="ore_mobs_42_check", callback=h_mobs_tier_callback,
                                             default_value=bool(4.2 in ore_mob_tiers))
                            dpg.add_checkbox(label="4.3", tag="ore_mobs_43_check", callback=h_mobs_tier_callback,
                                             default_value=bool(4.3 in ore_mob_tiers))
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="5", tag="ore_mobs_5_check", callback=h_mobs_tier_callback,
                                             default_value=bool(5 in ore_mob_tiers))
                            dpg.add_checkbox(label="5.1", tag="ore_mobs_51_check", callback=h_mobs_tier_callback,
                                             default_value=bool(5.1 in ore_mob_tiers))
                            dpg.add_checkbox(label="5.2", tag="ore_mobs_52_check", callback=h_mobs_tier_callback,
                                             default_value=bool(5.2 in ore_mob_tiers))
                            dpg.add_checkbox(label="5.3", tag="ore_mobs_53_check", callback=h_mobs_tier_callback,
                                             default_value=bool(5.3 in ore_mob_tiers))
                            dpg.add_checkbox(label="6", tag="ore_mobs_6_check", callback=h_mobs_tier_callback,
                                             default_value=bool(6 in ore_mob_tiers))
                            dpg.add_checkbox(label="6.1", tag="ore_mobs_61_check", callback=h_mobs_tier_callback,
                                             default_value=bool(6.1 in ore_mob_tiers))
                            dpg.add_checkbox(label="6.2", tag="ore_mobs_62_check", callback=h_mobs_tier_callback,
                                             default_value=bool(6.2 in ore_mob_tiers))
                            dpg.add_checkbox(label="6.3", tag="ore_mobs_63_check", callback=h_mobs_tier_callback,
                                             default_value=bool(6.3 in ore_mob_tiers))
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="7", tag="ore_mobs_7_check", callback=h_mobs_tier_callback,
                                             default_value=bool(7 in ore_mob_tiers))
                            dpg.add_checkbox(label="7.1", tag="ore_mobs_71_check", callback=h_mobs_tier_callback,
                                             default_value=bool(7.1 in ore_mob_tiers))
                            dpg.add_checkbox(label="7.2", tag="ore_mobs_72_check", callback=h_mobs_tier_callback,
                                             default_value=bool(7.2 in ore_mob_tiers))
                            dpg.add_checkbox(label="7.3", tag="ore_mobs_73_check", callback=h_mobs_tier_callback,
                                             default_value=bool(7.3 in ore_mob_tiers))
                            dpg.add_checkbox(label="8", tag="ore_mobs_8_check", callback=h_mobs_tier_callback,
                                             default_value=bool(8 in ore_mob_tiers))
                            dpg.add_checkbox(label="8.1", tag="ore_mobs_81_check", callback=h_mobs_tier_callback,
                                             default_value=bool(8.1 in ore_mob_tiers))
                            dpg.add_checkbox(label="8.2", tag="ore_mobs_82_check", callback=h_mobs_tier_callback,
                                             default_value=bool(8.2 in ore_mob_tiers))
                            dpg.add_checkbox(label="8.3", tag="ore_mobs_83_check", callback=h_mobs_tier_callback,
                                             default_value=bool(8.3 in ore_mob_tiers))

                    with dpg.tab(tag="tab_hide_mobs", label="Hide", show=bool("HIDE" in settings['hTypes'])):
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="1", tag="hide_mobs_1_check", callback=h_mobs_tier_callback,
                                             default_value=bool(1 in hide_mob_tiers))
                            dpg.add_checkbox(label="2", tag="hide_mobs_2_check", callback=h_mobs_tier_callback,
                                             default_value=bool(2 in hide_mob_tiers))
                            dpg.add_checkbox(label="3", tag="hide_mobs_3_check", callback=h_mobs_tier_callback,
                                             default_value=bool(3 in hide_mob_tiers))
                            dpg.add_checkbox(label="4", tag="hide_mobs_4_check", callback=h_mobs_tier_callback,
                                             default_value=bool(4 in hide_mob_tiers))
                            dpg.add_checkbox(label="4.1", tag="hide_mobs_41_check", callback=h_mobs_tier_callback,
                                             default_value=bool(4.1 in hide_mob_tiers))
                            dpg.add_checkbox(label="4.2", tag="hide_mobs_42_check", callback=h_mobs_tier_callback,
                                             default_value=bool(4.2 in hide_mob_tiers))
                            dpg.add_checkbox(label="4.3", tag="hide_mobs_43_check", callback=h_mobs_tier_callback,
                                             default_value=bool(4.3 in hide_mob_tiers))
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="5", tag="hide_mobs_5_check", callback=h_mobs_tier_callback,
                                             default_value=bool(5 in hide_mob_tiers))
                            dpg.add_checkbox(label="5.1", tag="hide_mobs_51_check", callback=h_mobs_tier_callback,
                                             default_value=bool(5.1 in hide_mob_tiers))
                            dpg.add_checkbox(label="5.2", tag="hide_mobs_52_check", callback=h_mobs_tier_callback,
                                             default_value=bool(5.2 in hide_mob_tiers))
                            dpg.add_checkbox(label="5.3", tag="hide_mobs_53_check", callback=h_mobs_tier_callback,
                                             default_value=bool(5.3 in hide_mob_tiers))
                            dpg.add_checkbox(label="6", tag="hide_mobs_6_check", callback=h_mobs_tier_callback,
                                             default_value=bool(6 in hide_mob_tiers))
                            dpg.add_checkbox(label="6.1", tag="hide_mobs_61_check", callback=h_mobs_tier_callback,
                                             default_value=bool(6.1 in hide_mob_tiers))
                            dpg.add_checkbox(label="6.2", tag="hide_mobs_62_check", callback=h_mobs_tier_callback,
                                             default_value=bool(6.2 in hide_mob_tiers))
                            dpg.add_checkbox(label="6.3", tag="hide_mobs_63_check", callback=h_mobs_tier_callback,
                                             default_value=bool(6.3 in hide_mob_tiers))
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="7", tag="hide_mobs_7_check", callback=h_mobs_tier_callback,
                                             default_value=bool(7 in hide_mob_tiers))
                            dpg.add_checkbox(label="7.1", tag="hide_mobs_71_check", callback=h_mobs_tier_callback,
                                             default_value=bool(7.1 in hide_mob_tiers))
                            dpg.add_checkbox(label="7.2", tag="hide_mobs_72_check", callback=h_mobs_tier_callback,
                                             default_value=bool(7.2 in hide_mob_tiers))
                            dpg.add_checkbox(label="7.3", tag="hide_mobs_73_check", callback=h_mobs_tier_callback,
                                             default_value=bool(7.3 in hide_mob_tiers))
                            dpg.add_checkbox(label="8", tag="hide_mobs_8_check", callback=h_mobs_tier_callback,
                                             default_value=bool(8 in hide_mob_tiers))
                            dpg.add_checkbox(label="8.1", tag="hide_mobs_81_check", callback=h_mobs_tier_callback,
                                             default_value=bool(8.1 in hide_mob_tiers))
                            dpg.add_checkbox(label="8.2", tag="hide_mobs_82_check", callback=h_mobs_tier_callback,
                                             default_value=bool(8.2 in hide_mob_tiers))
                            dpg.add_checkbox(label="8.3", tag="hide_mobs_83_check", callback=h_mobs_tier_callback,
                                             default_value=bool(8.3 in hide_mob_tiers))

                    with dpg.tab(tag="tab_fiber_mobs", label="Fiber", show=bool("FIBER" in settings['hTypes'])):
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="1", tag="fiber_mobs_1_check", callback=h_mobs_tier_callback,
                                             default_value=bool(1 in fiber_mob_tiers))
                            dpg.add_checkbox(label="2", tag="fiber_mobs_2_check", callback=h_mobs_tier_callback,
                                             default_value=bool(2 in fiber_mob_tiers))
                            dpg.add_checkbox(label="3", tag="fiber_mobs_3_check", callback=h_mobs_tier_callback,
                                             default_value=bool(3 in fiber_mob_tiers))
                            dpg.add_checkbox(label="4", tag="fiber_mobs_4_check", callback=h_mobs_tier_callback,
                                             default_value=bool(4 in fiber_mob_tiers))
                            dpg.add_checkbox(label="4.1", tag="fiber_mobs_41_check", callback=h_mobs_tier_callback,
                                             default_value=bool(4.1 in fiber_mob_tiers))
                            dpg.add_checkbox(label="4.2", tag="fiber_mobs_42_check", callback=h_mobs_tier_callback,
                                             default_value=bool(4.2 in fiber_mob_tiers))
                            dpg.add_checkbox(label="4.3", tag="fiber_mobs_43_check", callback=h_mobs_tier_callback,
                                             default_value=bool(4.3 in fiber_mob_tiers))
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="5", tag="fiber_mobs_5_check", callback=h_mobs_tier_callback,
                                             default_value=bool(5 in fiber_mob_tiers))
                            dpg.add_checkbox(label="5.1", tag="fiber_mobs_51_check", callback=h_mobs_tier_callback,
                                             default_value=bool(5.1 in fiber_mob_tiers))
                            dpg.add_checkbox(label="5.2", tag="fiber_mobs_52_check", callback=h_mobs_tier_callback,
                                             default_value=bool(5.2 in fiber_mob_tiers))
                            dpg.add_checkbox(label="5.3", tag="fiber_mobs_53_check", callback=h_mobs_tier_callback,
                                             default_value=bool(5.3 in fiber_mob_tiers))
                            dpg.add_checkbox(label="6", tag="fiber_mobs_6_check", callback=h_mobs_tier_callback,
                                             default_value=bool(6 in fiber_mob_tiers))
                            dpg.add_checkbox(label="6.1", tag="fiber_mobs_61_check", callback=h_mobs_tier_callback,
                                             default_value=bool(6.1 in fiber_mob_tiers))
                            dpg.add_checkbox(label="6.2", tag="fiber_mobs_62_check", callback=h_mobs_tier_callback,
                                             default_value=bool(6.2 in fiber_mob_tiers))
                            dpg.add_checkbox(label="6.3", tag="fiber_mobs_63_check", callback=h_mobs_tier_callback,
                                             default_value=bool(6.3 in fiber_mob_tiers))
                        with dpg.group(horizontal=True):
                            dpg.add_checkbox(label="7", tag="fiber_mobs_7_check", callback=h_mobs_tier_callback,
                                             default_value=bool(7 in fiber_mob_tiers))
                            dpg.add_checkbox(label="7.1", tag="fiber_mobs_71_check", callback=h_mobs_tier_callback,
                                             default_value=bool(7.1 in fiber_mob_tiers))
                            dpg.add_checkbox(label="7.2", tag="fiber_mobs_72_check", callback=h_mobs_tier_callback,
                                             default_value=bool(7.2 in fiber_mob_tiers))
                            dpg.add_checkbox(label="7.3", tag="fiber_mobs_73_check", callback=h_mobs_tier_callback,
                                             default_value=bool(7.3 in fiber_mob_tiers))
                            dpg.add_checkbox(label="8", tag="fiber_mobs_8_check", callback=h_mobs_tier_callback,
                                             default_value=bool(8 in fiber_mob_tiers))
                            dpg.add_checkbox(label="8.1", tag="fiber_mobs_81_check", callback=h_mobs_tier_callback,
                                             default_value=bool(8.1 in fiber_mob_tiers))
                            dpg.add_checkbox(label="8.2", tag="fiber_mobs_82_check", callback=h_mobs_tier_callback,
                                             default_value=bool(8.2 in fiber_mob_tiers))
                            dpg.add_checkbox(label="8.3", tag="fiber_mobs_83_check", callback=h_mobs_tier_callback,
                                             default_value=bool(8.3 in fiber_mob_tiers))

            with dpg.tab(tag="tab_combat", label="Combat"):
                with dpg.table(tag="tbl_combat", height=24, scrollY=True, header_row=False):
                    dpg.add_table_column(tag="combat_text", width_fixed=True)
                    dpg.add_table_column(tag="combat_input", width_stretch=True)

                    with dpg.table_row():
                        dpg.add_text("Low health: ")
                        dpg.add_input_int(tag="low_health", default_value=settings['lowHealth'], max_value=10000, min_clamped=True, max_clamped=True)
                dpg.add_text("Skills")
                with dpg.tab_bar(tag="skills_tab_bar"):
                    with dpg.tab(tag="q_tab", label="Q"):
                        with dpg.table(tag="tbl_q", scrollY=True, header_row=False):
                            dpg.add_table_column(tag="q_text", width_fixed=True)
                            dpg.add_table_column(tag="q_input", width_stretch=True)

                            with dpg.table_row():
                                dpg.add_text("Cooldown: ")
                                dpg.add_input_float(tag="q_cooldown", default_value=settings['q_skill_cooldown'], max_value=1000, min_clamped=True, max_clamped=True, format='%.2f')
                            with dpg.table_row():
                                dpg.add_text("Max Uses: ")
                                dpg.add_input_int(tag="q_max_uses", default_value=settings['q_skill_max_uses'], max_value=10, min_clamped=True, max_clamped=True)
                            with dpg.table_row():
                                dpg.add_text("Channeling: ")
                                dpg.add_input_float(tag="q_channeling", default_value=settings['q_skill_channel_time'], max_value=100, min_clamped=True, max_clamped=True, format='%.2f')
                            with dpg.table_row():
                                dpg.add_text("Must Target?: ")
                                dpg.add_checkbox(tag="q_must_target", default_value=settings['q_skill_must_target'])

                    with dpg.tab(tag="w_tab", label="W"):
                        with dpg.table(tag="tbl_w", scrollY=True, header_row=False):
                            dpg.add_table_column(tag="w_text", width_fixed=True)
                            dpg.add_table_column(tag="w_input", width_stretch=True)

                            with dpg.table_row():
                                dpg.add_text("Cooldown: ")
                                dpg.add_input_float(tag="w_cooldown", default_value=settings['w_skill_cooldown'], max_value=1000, min_clamped=True, max_clamped=True, format='%.2f')
                            with dpg.table_row():
                                dpg.add_text("Max Uses: ")
                                dpg.add_input_int(tag="w_max_uses", default_value=settings['w_skill_max_uses'], max_value=10, min_clamped=True, max_clamped=True)
                            with dpg.table_row():
                                dpg.add_text("Channeling: ")
                                dpg.add_input_float(tag="w_channeling", default_value=settings['w_skill_channel_time'], max_value=100, min_clamped=True, max_clamped=True, format='%.2f')
                            with dpg.table_row():
                                dpg.add_text("Must Target?: ")
                                dpg.add_checkbox(tag="w_must_target", default_value=settings['w_skill_must_target'])

                    with dpg.tab(tag="e_tab", label="E"):
                        with dpg.table(tag="tbl_e", scrollY=True, header_row=False):
                            dpg.add_table_column(tag="e_text", width_fixed=True)
                            dpg.add_table_column(tag="e_input", width_stretch=True)

                            with dpg.table_row():
                                dpg.add_text("Cooldown: ")
                                dpg.add_input_float(tag="e_cooldown", default_value=settings['e_skill_cooldown'], max_value=1000, min_clamped=True, max_clamped=True, format='%.2f')
                            with dpg.table_row():
                                dpg.add_text("Max Uses: ")
                                dpg.add_input_int(tag="e_max_uses", default_value=settings['e_skill_max_uses'], max_value=10, min_clamped=True, max_clamped=True)
                            with dpg.table_row():
                                dpg.add_text("Channeling: ")
                                dpg.add_input_float(tag="e_channeling", default_value=settings['e_skill_channel_time'], max_value=100, min_clamped=True, max_clamped=True, format='%.2f')
                            with dpg.table_row():
                                dpg.add_text("Must Target?: ")
                                dpg.add_checkbox(tag="e_must_target", default_value=settings['e_skill_must_target'])

                    with dpg.tab(tag="r_tab", label="R"):
                        with dpg.table(tag="tbl_r", scrollY=True, header_row=False):
                            dpg.add_table_column(tag="r_text", width_fixed=True)
                            dpg.add_table_column(tag="r_input", width_stretch=True)

                            with dpg.table_row():
                                dpg.add_text("Cooldown: ")
                                dpg.add_input_float(tag="r_cooldown", default_value=settings['r_skill_cooldown'], max_value=1000, min_clamped=True, max_clamped=True, format='%.2f')
                            with dpg.table_row():
                                dpg.add_text("Max Uses: ")
                                dpg.add_input_int(tag="r_max_uses", default_value=settings['r_skill_max_uses'], max_value=10, min_clamped=True, max_clamped=True)
                            with dpg.table_row():
                                dpg.add_text("Channeling: ")
                                dpg.add_input_float(tag="r_channeling", default_value=settings['r_skill_channel_time'], max_value=100, min_clamped=True, max_clamped=True, format='%.2f')
                            with dpg.table_row():
                                dpg.add_text("Must Target?: ")
                                dpg.add_checkbox(tag="r_must_target", default_value=settings['r_skill_must_target'])

            with dpg.tab(tag="tab_apis", label="APIs"):
                with dpg.table(tag="tbl_apis", scrollY=True, header_row=False):
                    dpg.add_table_column(tag="apis_text", width_fixed=True)
                    dpg.add_table_column(tag="apis_input", width_stretch=True)

                    with dpg.table_row():
                        dpg.add_text("Dashboard API IP: ")
                        dpg.add_input_text(tag="api_ip", default_value=settings['API_SERVER'])
                    with dpg.table_row():
                        dpg.add_text("Telegram API Key: ")
                        dpg.add_input_text(tag="api_key", default_value=settings['API_KEY'])
                    with dpg.table_row():
                        dpg.add_text("Telegram Chat ID: ")
                        dpg.add_input_text(tag="chat_id", default_value=settings['CHAT_ID'])
                    with dpg.table_row():
                        dpg.add_text("Bot Name: ")
                        dpg.add_input_text(tag="bot_name", default_value=settings['BOT_NAME'])


# Main Excecution
dpg.set_primary_window("main_window", True)
dpg.set_viewport_vsync(True)
dpg.set_viewport_resizable(False)
# dpg.show_style_editor()
theme = create_theme_imgui_dark()
dpg.bind_theme(theme)

dpg.setup_dearpygui()
dpg.show_viewport()

while dpg.is_dearpygui_running():
    try:
        dpg.render_dearpygui_frame()
    except KeyboardInterrupt:
        break

dpg.destroy_context()
os._exit(0)

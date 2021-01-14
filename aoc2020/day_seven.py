"""
# Advent of code 2020
# Day 7
# https://adventofcode.com/2020/day/7
"""

# VIM search and replace:
# :%s/\./']/g
# :%s/ contain / = ['/g
# :%s/g, /g', '/g
# :%s/gs, /gs', '/g
# :%s/bags/bag/g
# :%s/ /_/g
# :%s/,_/, /g
# :%s/_=_/ = /g

# On copy of original data to get BAGS:
# :%s/s contain.*//g
# :%s/\n/, /g
# :%s/ /_/g
# :%s/,_/, /g

drab_tan_bag = ['4_clear_gold_bag']
vibrant_lime_bag = [
    '3_faded_gold_bag', '3_plaid_aqua_bag', '2_clear_black_bag'
]
pale_lime_bag = [
    '1_dim_salmon_bag', '5_faded_salmon_bag', '1_dim_turquoise_bag'
]
dull_gray_bag = ['1_striped_gold_bag', '1_vibrant_yellow_bag']
light_fuchsia_bag = [
    '4_light_lavender_bag', '5_faded_olive_bag', '4_plaid_cyan_bag',
    '1_striped_tomato_bag'
]
drab_gold_bag = ['1_clear_teal_bag']
dim_red_bag = ['2_dull_teal_bag']
striped_orange_bag = [
    '1_bright_fuchsia_bag', '3_plaid_chartreuse_bag', '4_dark_silver_bag',
    '5_dim_maroon_bag'
]
shiny_violet_bag = [
    '1_clear_orange_bag', '4_muted_olive_bag', '4_dark_chartreuse_bag',
    '4_shiny_indigo_bag'
]
faded_olive_bag = ['2_dotted_silver_bag', '4_clear_gray_bag']
dotted_lime_bag = [
    '1_dark_turquoise_bag', '1_striped_orange_bag', '2_shiny_teal_bag',
    '2_vibrant_cyan_bag'
]
drab_magenta_bag = [
    '4_bright_yellow_bag', '5_dull_orange_bag', '5_plaid_tomato_bag'
]
dull_black_bag = ['4_light_olive_bag']
posh_turquoise_bag = [
    '1_muted_salmon_bag', '1_muted_black_bag', '5_shiny_turquoise_bag'
]
muted_purple_bag = ['5_dotted_red_bag']
striped_black_bag = [
    '1_striped_fuchsia_bag', '4_drab_indigo_bag', '3_dark_turquoise_bag'
]
drab_brown_bag = ['3_clear_gray_bag', '1_light_gray_bag', '1_dull_coral_bag']
pale_purple_bag = ['5_mirrored_black_bag', '4_wavy_crimson_bag']
dark_turquoise_bag = ['1_dotted_violet_bag']
clear_lavender_bag = [
    '1_light_olive_bag', '4_wavy_yellow_bag', '4_plaid_red_bag',
    '2_faded_salmon_bag'
]
bright_coral_bag = ['2_bright_brown_bag']
posh_coral_bag = ['4_dull_teal_bag', '4_bright_aqua_bag']
drab_lime_bag = ['4_striped_tan_bag', '4_muted_violet_bag']
striped_brown_bag = ['1_dark_lime_bag', '4_clear_orange_bag']
wavy_bronze_bag = ['2_posh_coral_bag', '3_mirrored_silver_bag']
dim_black_bag = [
    '1_dark_maroon_bag', '4_muted_lavender_bag', '3_bright_cyan_bag',
    '3_dark_plum_bag'
]
posh_yellow_bag = ['4_dull_plum_bag', '5_shiny_blue_bag', '3_plaid_tomato_bag']
pale_violet_bag = ['1_plaid_red_bag', '2_posh_fuchsia_bag']
mirrored_bronze_bag = ['4_striped_lavender_bag']
vibrant_silver_bag = [
    '4_posh_brown_bag', '4_clear_indigo_bag', '4_dotted_silver_bag',
    '5_drab_lavender_bag'
]
dark_brown_bag = [
    '1_mirrored_plum_bag', '1_muted_violet_bag', '3_muted_tomato_bag'
]
wavy_green_bag = ['2_posh_bronze_bag', '3_dull_purple_bag', '1_wavy_red_bag']
light_beige_bag = [
    '3_light_maroon_bag', '3_vibrant_orange_bag', '4_clear_blue_bag',
    '3_mirrored_fuchsia_bag'
]
wavy_crimson_bag = ['5_muted_beige_bag', '2_dark_olive_bag']
clear_tan_bag = ['1_wavy_yellow_bag']
posh_lime_bag = ['3_wavy_beige_bag']
pale_blue_bag = [
    '5_dull_aqua_bag', '4_pale_crimson_bag', '4_clear_indigo_bag',
    '3_dull_lime_bag'
]
wavy_silver_bag = ['1_pale_cyan_bag']
striped_beige_bag = ['4_dim_plum_bag', '1_clear_gray_bag']
dim_gold_bag = ['3_dull_cyan_bag', '3_drab_black_bag', '4_dark_green_bag']
vibrant_teal_bag = [
    '5_clear_green_bag', '4_light_violet_bag', '2_bright_beige_bag'
]
light_tan_bag = [
    '5_pale_red_bag', '3_light_turquoise_bag', '2_mirrored_chartreuse_bag'
]
dark_red_bag = ['5_shiny_lime_bag', '3_clear_blue_bag', '1_posh_black_bag']
posh_salmon_bag = [
    '1_vibrant_silver_bag', '1_plaid_salmon_bag', '5_dark_turquoise_bag',
    '1_shiny_orange_bag'
]
mirrored_yellow_bag = [
    '5_posh_gray_bag', '1_shiny_silver_bag', '1_dark_brown_bag'
]
dark_fuchsia_bag = ['1_plaid_plum_bag']
bright_bronze_bag = ['4_dark_turquoise_bag']
posh_silver_bag = [
    '1_muted_gold_bag', '3_dull_aqua_bag', '2_striped_chartreuse_bag',
    '3_posh_gray_bag'
]
dotted_salmon_bag = [
    '2_vibrant_bronze_bag', '3_striped_blue_bag', '4_striped_fuchsia_bag'
]
dark_orange_bag = ['5_faded_magenta_bag']
bright_silver_bag = ['5_drab_silver_bag']
posh_orange_bag = ['4_plaid_tan_bag', '5_light_tan_bag']
mirrored_olive_bag = [
    '4_dull_cyan_bag', '4_posh_black_bag', '2_striped_chartreuse_bag'
]
drab_beige_bag = ['2_dark_green_bag', '2_bright_maroon_bag']
muted_bronze_bag = ['2_clear_indigo_bag', '1_clear_green_bag']
dark_lime_bag = ['3_wavy_brown_bag']
dark_olive_bag = ['4_muted_gold_bag', '1_shiny_chartreuse_bag']
dull_white_bag = ['2_muted_crimson_bag', '1_light_maroon_bag']
shiny_gray_bag = ['1_striped_orange_bag', '2_dim_maroon_bag']
dotted_orange_bag = [
    '1_dull_teal_bag', '1_light_salmon_bag', '4_shiny_brown_bag',
    '4_muted_salmon_bag'
]
clear_olive_bag = ['3_mirrored_tan_bag', '5_pale_tan_bag']
drab_bronze_bag = ['1_drab_teal_bag', '1_dark_green_bag']
drab_chartreuse_bag = ['4_dim_beige_bag']
faded_cyan_bag = ['5_clear_gold_bag']
plaid_fuchsia_bag = ['2_pale_yellow_bag']
light_gold_bag = [
    '5_pale_cyan_bag', '1_posh_olive_bag', '2_faded_salmon_bag',
    '5_pale_tomato_bag'
]
pale_bronze_bag = ['2_posh_white_bag']
shiny_coral_bag = ['2_plaid_crimson_bag', '1_clear_turquoise_bag']
vibrant_green_bag = [
    '4_shiny_gold_bag', '2_dim_orange_bag', '3_plaid_chartreuse_bag',
    '4_dark_tomato_bag'
]
vibrant_violet_bag = ['5_bright_aqua_bag', '5_clear_purple_bag']
muted_fuchsia_bag = ['2_bright_yellow_bag']
bright_olive_bag = [
    '5_bright_gold_bag', '5_plaid_aqua_bag', '5_dull_black_bag',
    '1_mirrored_indigo_bag'
]
mirrored_maroon_bag = ['2_dull_chartreuse_bag']
pale_salmon_bag = [
    '1_muted_gold_bag', '5_bright_red_bag', '5_mirrored_tan_bag',
    '1_muted_salmon_bag'
]
faded_brown_bag = [
    '3_plaid_tomato_bag', '2_muted_olive_bag', '5_dull_orange_bag',
    '2_dark_silver_bag'
]
dark_lavender_bag = [
    '4_dark_tomato_bag', '2_drab_plum_bag', '3_vibrant_gray_bag',
    '1_dim_gold_bag'
]
plaid_coral_bag = ['3_striped_turquoise_bag', '2_faded_salmon_bag']
drab_black_bag = ['1_vibrant_black_bag']
shiny_black_bag = [
    '3_posh_gray_bag', '3_shiny_olive_bag', '4_dull_violet_bag',
    '4_vibrant_plum_bag'
]
muted_plum_bag = [
    '4_dull_violet_bag', '5_pale_tomato_bag', '1_shiny_brown_bag',
    '1_dark_plum_bag'
]
shiny_lavender_bag = ['4_mirrored_lavender_bag']
mirrored_blue_bag = ['1_faded_violet_bag', '2_plaid_olive_bag']
dotted_aqua_bag = ['3_shiny_yellow_bag']
light_lavender_bag = [
    '2_bright_maroon_bag', '4_shiny_lime_bag', '3_dark_maroon_bag',
    '1_light_silver_bag'
]
bright_orange_bag = ['3_striped_gold_bag', '5_dotted_violet_bag']
muted_tomato_bag = ['5_clear_blue_bag', '5_mirrored_fuchsia_bag']
dim_indigo_bag = ['1_pale_olive_bag', '1_light_indigo_bag', '5_posh_brown_bag']
faded_turquoise_bag = ['3_pale_chartreuse_bag', '4_light_olive_bag']
wavy_teal_bag = ['3_clear_brown_bag', '3_dark_beige_bag']
dotted_bronze_bag = ['1_wavy_brown_bag']
posh_purple_bag = [
    '5_bright_maroon_bag', '1_clear_silver_bag', '2_shiny_indigo_bag'
]
dull_violet_bag = ['1_vibrant_black_bag']
drab_indigo_bag = ['4_light_beige_bag']
mirrored_crimson_bag = [
    '4_plaid_bronze_bag', '3_pale_chartreuse_bag', '2_mirrored_olive_bag',
    '4_muted_lavender_bag'
]
mirrored_tan_bag = ['2_posh_brown_bag', '3_dark_red_bag', '3_faded_salmon_bag']
wavy_fuchsia_bag = [
    '2_pale_crimson_bag', '1_plaid_magenta_bag', '2_drab_plum_bag',
    '1_drab_aqua_bag'
]
striped_yellow_bag = ['4_dark_coral_bag', '5_dim_silver_bag']
striped_white_bag = [
    '4_faded_teal_bag', '2_posh_black_bag', '3_vibrant_yellow_bag',
    '1_faded_yellow_bag'
]
light_turquoise_bag = [
    '4_dark_red_bag', '5_posh_white_bag', '1_vibrant_bronze_bag'
]
clear_blue_bag = ['no_other_bag']
faded_blue_bag = [
    '5_clear_indigo_bag', '4_muted_salmon_bag', '3_bright_violet_bag',
    '4_dark_purple_bag'
]
dim_aqua_bag = [
    '4_posh_gray_bag', '1_clear_bronze_bag', '4_dull_magenta_bag',
    '5_plaid_red_bag'
]
shiny_magenta_bag = ['2_mirrored_teal_bag']
wavy_maroon_bag = [
    '1_dull_cyan_bag', '2_striped_yellow_bag', '2_light_turquoise_bag'
]
plaid_teal_bag = [
    '5_light_olive_bag', '2_vibrant_green_bag', '4_plaid_yellow_bag'
]
bright_tomato_bag = [
    '3_bright_maroon_bag', '3_clear_blue_bag', '5_posh_lavender_bag',
    '5_shiny_lime_bag'
]
mirrored_lavender_bag = [
    '5_striped_bronze_bag', '4_drab_plum_bag', '1_faded_violet_bag',
    '5_bright_maroon_bag'
]
vibrant_purple_bag = ['1_dull_plum_bag', '4_wavy_yellow_bag']
posh_aqua_bag = ['2_plaid_teal_bag', '3_pale_tomato_bag', '4_muted_teal_bag']
faded_fuchsia_bag = [
    '3_dark_lavender_bag', '4_plaid_green_bag', '5_drab_gold_bag'
]
dim_silver_bag = ['1_vibrant_yellow_bag', '1_clear_tomato_bag']
bright_brown_bag = ['3_striped_white_bag', '4_shiny_orange_bag']
dim_olive_bag = [
    '2_clear_violet_bag', '3_plaid_gold_bag', '3_plaid_lime_bag',
    '4_dim_plum_bag'
]
striped_teal_bag = [
    '2_bright_lavender_bag', '5_faded_beige_bag', '5_clear_beige_bag',
    '4_dotted_turquoise_bag'
]
posh_plum_bag = ['3_bright_brown_bag']
faded_teal_bag = [
    '4_bright_aqua_bag', '2_bright_red_bag', '2_dotted_beige_bag',
    '5_shiny_teal_bag'
]
striped_indigo_bag = [
    '5_clear_cyan_bag', '3_clear_gray_bag', '4_plaid_olive_bag',
    '3_plaid_lime_bag'
]
drab_blue_bag = ['2_dim_coral_bag', '4_plaid_purple_bag']
light_olive_bag = ['1_clear_purple_bag', '4_clear_blue_bag']
vibrant_red_bag = ['2_bright_red_bag', '2_pale_gray_bag', '4_wavy_tomato_bag']
faded_salmon_bag = ['5_posh_brown_bag']
shiny_brown_bag = ['2_dull_green_bag', '3_wavy_lime_bag']
posh_olive_bag = ['5_mirrored_lavender_bag', '3_clear_gray_bag']
clear_green_bag = [
    '2_faded_aqua_bag', '3_vibrant_olive_bag', '4_dim_orange_bag'
]
mirrored_violet_bag = ['5_wavy_lime_bag', '1_wavy_chartreuse_bag']
light_brown_bag = ['5_dark_lavender_bag']
plaid_blue_bag = ['3_plaid_beige_bag', '5_dotted_teal_bag']
dim_green_bag = ['1_light_gray_bag', '5_bright_green_bag']
mirrored_plum_bag = ['1_dark_turquoise_bag', '1_plaid_black_bag']
dotted_turquoise_bag = ['1_clear_purple_bag', '2_bright_fuchsia_bag']
dull_salmon_bag = ['3_faded_lime_bag', '1_striped_gray_bag', '3_dull_gold_bag']
wavy_plum_bag = [
    '4_shiny_green_bag', '3_pale_tomato_bag', '2_dull_crimson_bag'
]
bright_blue_bag = ['5_dull_lavender_bag', '5_drab_black_bag']
posh_tomato_bag = [
    '4_clear_turquoise_bag', '2_dim_chartreuse_bag', '4_bright_aqua_bag'
]
dotted_lavender_bag = ['4_wavy_red_bag']
posh_magenta_bag = ['3_light_olive_bag']
faded_beige_bag = [
    '5_muted_olive_bag', '4_bright_maroon_bag', '1_bright_fuchsia_bag'
]
vibrant_plum_bag = ['4_plaid_crimson_bag', '3_faded_turquoise_bag']
pale_green_bag = [
    '3_wavy_tomato_bag', '4_plaid_indigo_bag', '3_pale_crimson_bag'
]
dull_fuchsia_bag = ['2_clear_gold_bag']
light_plum_bag = ['5_dark_plum_bag', '1_striped_white_bag']
dotted_olive_bag = ['5_vibrant_maroon_bag']
striped_gold_bag = [
    '1_dull_lime_bag', '3_clear_blue_bag', '5_vibrant_cyan_bag'
]
bright_violet_bag = ['1_shiny_lime_bag', '1_muted_tomato_bag']
dim_yellow_bag = ['2_dull_green_bag']
bright_indigo_bag = [
    '4_light_salmon_bag', '3_wavy_lavender_bag', '3_light_gold_bag',
    '4_plaid_olive_bag'
]
plaid_lime_bag = ['5_plaid_crimson_bag', '5_dark_bronze_bag']
striped_aqua_bag = [
    '5_dark_olive_bag', '4_dull_tomato_bag', '5_pale_gold_bag',
    '1_dark_silver_bag'
]
dull_maroon_bag = [
    '2_pale_teal_bag', '5_light_coral_bag', '4_light_magenta_bag'
]
muted_tan_bag = [
    '2_clear_yellow_bag', '4_plaid_indigo_bag', '2_dotted_crimson_bag',
    '2_dim_plum_bag'
]
plaid_tan_bag = ['1_wavy_beige_bag', '4_dark_chartreuse_bag']
dull_beige_bag = [
    '3_posh_cyan_bag', '3_posh_yellow_bag', '4_wavy_green_bag',
    '1_striped_brown_bag'
]
posh_cyan_bag = ['1_faded_yellow_bag', '5_dark_coral_bag']
drab_red_bag = ['2_wavy_lime_bag', '2_posh_brown_bag']
drab_gray_bag = ['1_mirrored_yellow_bag', '2_plaid_turquoise_bag']
muted_red_bag = ['1_shiny_silver_bag', '2_pale_coral_bag', '5_dull_plum_bag']
drab_green_bag = [
    '4_shiny_brown_bag', '3_striped_yellow_bag', '5_clear_blue_bag'
]
dim_gray_bag = ['5_wavy_maroon_bag', '3_light_tomato_bag', '1_dim_plum_bag']
dark_white_bag = ['3_light_brown_bag']
posh_black_bag = ['no_other_bag']
dim_turquoise_bag = ['3_dull_fuchsia_bag', '2_dull_black_bag']
drab_lavender_bag = ['3_pale_maroon_bag']
striped_crimson_bag = ['5_light_coral_bag']
vibrant_olive_bag = ['4_vibrant_gold_bag']
dim_maroon_bag = [
    '4_drab_red_bag', '3_pale_salmon_bag', '1_mirrored_fuchsia_bag',
    '3_dim_coral_bag'
]
muted_lime_bag = ['4_drab_cyan_bag', '1_muted_beige_bag']
drab_purple_bag = ['4_dotted_gold_bag']
muted_beige_bag = [
    '1_vibrant_violet_bag', '2_light_lavender_bag', '4_wavy_maroon_bag'
]
dotted_green_bag = ['1_wavy_blue_bag']
bright_black_bag = ['4_wavy_chartreuse_bag', '1_clear_purple_bag']
wavy_yellow_bag = ['2_posh_lavender_bag', '5_faded_yellow_bag']
faded_yellow_bag = [
    '4_posh_black_bag', '2_bright_chartreuse_bag', '5_bright_fuchsia_bag'
]
dim_purple_bag = [
    '2_faded_lavender_bag', '3_bright_aqua_bag', '4_mirrored_fuchsia_bag',
    '5_posh_tomato_bag'
]
bright_chartreuse_bag = ['no_other_bag']
vibrant_maroon_bag = ['1_clear_gold_bag', '3_bright_purple_bag']
pale_fuchsia_bag = ['2_dark_magenta_bag']
dotted_teal_bag = ['5_shiny_chartreuse_bag']
dull_lime_bag = ['2_dotted_violet_bag', '3_vibrant_cyan_bag']
bright_salmon_bag = [
    '2_vibrant_coral_bag', '3_bright_gray_bag', '4_wavy_beige_bag',
    '1_faded_green_bag'
]
bright_magenta_bag = [
    '3_vibrant_crimson_bag', '1_striped_fuchsia_bag', '1_mirrored_maroon_bag'
]
striped_red_bag = [
    '4_vibrant_indigo_bag', '3_plaid_black_bag', '3_dark_coral_bag'
]
pale_teal_bag = [
    '3_shiny_purple_bag', '3_light_turquoise_bag', '5_bright_aqua_bag',
    '4_clear_blue_bag'
]
clear_cyan_bag = [
    '3_bright_maroon_bag', '3_shiny_purple_bag', '1_dark_green_bag',
    '5_muted_olive_bag'
]
muted_gray_bag = ['4_dark_teal_bag', '3_vibrant_coral_bag', '4_plaid_red_bag']
bright_gold_bag = [
    '2_faded_indigo_bag', '1_muted_beige_bag', '5_mirrored_orange_bag',
    '4_pale_green_bag'
]
clear_red_bag = ['3_plaid_tomato_bag', '2_dark_violet_bag']
striped_purple_bag = ['3_posh_lavender_bag']
plaid_violet_bag = ['5_mirrored_gold_bag']
shiny_crimson_bag = [
    '4_bright_black_bag', '2_wavy_purple_bag', '1_dark_crimson_bag'
]
posh_gold_bag = ['4_dull_yellow_bag']
dim_crimson_bag = ['3_drab_white_bag']
posh_red_bag = ['3_dull_green_bag', '1_striped_red_bag']
drab_turquoise_bag = [
    '5_clear_beige_bag', '3_dull_orange_bag', '3_shiny_green_bag',
    '5_dark_yellow_bag'
]
vibrant_cyan_bag = ['no_other_bag']
light_bronze_bag = [
    '3_plaid_magenta_bag', '2_pale_salmon_bag', '1_dim_orange_bag',
    '2_vibrant_blue_bag'
]
dotted_cyan_bag = ['1_faded_purple_bag', '4_drab_crimson_bag']
drab_fuchsia_bag = ['4_plaid_salmon_bag']
clear_maroon_bag = ['4_dotted_white_bag', '1_dark_olive_bag', '1_dull_red_bag']
dim_salmon_bag = ['4_light_green_bag', '2_drab_black_bag', '4_drab_lime_bag']
wavy_aqua_bag = ['5_dull_tan_bag', '4_plaid_crimson_bag']
pale_beige_bag = [
    '2_faded_lavender_bag', '5_striped_beige_bag', '1_light_teal_bag'
]
dark_maroon_bag = [
    '2_bright_tomato_bag', '2_striped_chartreuse_bag', '5_bright_maroon_bag'
]
light_aqua_bag = ['3_faded_yellow_bag']
dim_tan_bag = ['5_light_orange_bag', '5_dark_white_bag', '1_dull_green_bag']
vibrant_brown_bag = ['2_plaid_tomato_bag']
light_magenta_bag = [
    '5_dotted_violet_bag', '2_faded_crimson_bag', '3_bright_red_bag',
    '5_mirrored_turquoise_bag'
]
clear_turquoise_bag = [
    '3_striped_tan_bag', '2_mirrored_tan_bag', '4_plaid_black_bag'
]
dull_crimson_bag = [
    '2_faded_tomato_bag', '4_dotted_beige_bag', '5_dim_coral_bag',
    '3_shiny_coral_bag'
]
dull_orange_bag = [
    '5_muted_tomato_bag', '5_dull_lime_bag', '4_faded_salmon_bag',
    '5_bright_chartreuse_bag'
]
wavy_black_bag = ['3_dark_cyan_bag', '3_clear_red_bag']
plaid_olive_bag = [
    '1_mirrored_fuchsia_bag', '5_dull_purple_bag', '1_bright_fuchsia_bag'
]
plaid_indigo_bag = [
    '3_mirrored_tan_bag', '1_mirrored_olive_bag', '1_striped_turquoise_bag',
    '1_dotted_violet_bag'
]
dim_brown_bag = ['4_faded_teal_bag']
muted_indigo_bag = [
    '1_mirrored_plum_bag', '5_pale_gray_bag', '5_faded_salmon_bag'
]
dull_plum_bag = [
    '4_mirrored_cyan_bag', '2_light_coral_bag', '3_dark_violet_bag',
    '4_striped_fuchsia_bag'
]
vibrant_tan_bag = ['2_clear_white_bag', '1_dim_silver_bag']
plaid_tomato_bag = ['3_dark_green_bag']
shiny_white_bag = ['1_dotted_bronze_bag', '2_faded_gold_bag', '1_drab_tan_bag']
plaid_red_bag = [
    '2_pale_olive_bag', '2_muted_purple_bag', '3_mirrored_chartreuse_bag'
]
drab_orange_bag = ['3_bright_indigo_bag', '3_pale_salmon_bag']
striped_green_bag = [
    '4_pale_maroon_bag', '4_muted_brown_bag', '2_bright_tomato_bag'
]
shiny_indigo_bag = [
    '4_clear_teal_bag', '1_pale_teal_bag', '4_vibrant_purple_bag',
    '3_plaid_brown_bag'
]
drab_yellow_bag = [
    '5_faded_black_bag', '1_plaid_green_bag', '1_mirrored_plum_bag'
]
faded_magenta_bag = [
    '4_vibrant_indigo_bag', '2_shiny_gold_bag', '2_mirrored_lavender_bag'
]
muted_yellow_bag = [
    '4_light_turquoise_bag', '2_shiny_lime_bag', '2_striped_white_bag',
    '3_dark_silver_bag'
]
posh_brown_bag = ['3_dull_cyan_bag']
pale_tomato_bag = ['1_mirrored_fuchsia_bag']
dark_aqua_bag = ['4_dull_blue_bag', '5_mirrored_white_bag']
muted_blue_bag = ['3_mirrored_fuchsia_bag']
light_silver_bag = ['no_other_bag']
muted_coral_bag = [
    '1_pale_plum_bag', '2_wavy_crimson_bag', '5_posh_magenta_bag',
    '4_vibrant_brown_bag'
]
muted_green_bag = [
    '4_shiny_gray_bag', '4_pale_crimson_bag', '4_striped_yellow_bag',
    '1_bright_salmon_bag'
]
muted_brown_bag = ['2_dark_lavender_bag', '2_dim_chartreuse_bag']
dim_violet_bag = ['4_faded_tan_bag', '3_dull_violet_bag', '1_light_yellow_bag']
clear_fuchsia_bag = ['2_drab_plum_bag']
muted_violet_bag = [
    '3_muted_salmon_bag', '1_clear_tomato_bag', '1_dark_red_bag'
]
posh_violet_bag = [
    '5_dull_chartreuse_bag', '2_light_coral_bag', '5_mirrored_cyan_bag'
]
dark_violet_bag = [
    '1_vibrant_bronze_bag', '4_bright_red_bag', '3_striped_gold_bag'
]
dotted_fuchsia_bag = [
    '2_vibrant_tan_bag', '5_striped_crimson_bag', '3_wavy_silver_bag'
]
vibrant_indigo_bag = [
    '3_bright_fuchsia_bag', '2_muted_gold_bag', '1_bright_red_bag',
    '3_bright_aqua_bag'
]
vibrant_gray_bag = ['3_vibrant_yellow_bag', '2_clear_teal_bag']
dotted_plum_bag = [
    '5_dull_crimson_bag', '2_posh_green_bag', '2_light_gray_bag',
    '2_pale_tomato_bag'
]
vibrant_magenta_bag = ['4_dotted_beige_bag']
drab_maroon_bag = ['1_drab_coral_bag', '1_dotted_tan_bag', '1_dull_cyan_bag']
dotted_gold_bag = ['1_wavy_yellow_bag', '4_dark_olive_bag']
striped_cyan_bag = [
    '4_shiny_gold_bag', '5_striped_crimson_bag', '5_striped_red_bag'
]
pale_silver_bag = ['5_vibrant_red_bag', '4_clear_red_bag']
drab_coral_bag = [
    '4_striped_gold_bag', '5_striped_silver_bag', '4_mirrored_turquoise_bag',
    '5_striped_turquoise_bag'
]
vibrant_chartreuse_bag = [
    '5_striped_gray_bag', '1_bright_turquoise_bag', '1_shiny_silver_bag'
]
pale_maroon_bag = [
    '5_vibrant_bronze_bag', '4_bright_tan_bag', '2_clear_gray_bag',
    '4_light_turquoise_bag'
]
wavy_blue_bag = ['4_wavy_yellow_bag']
mirrored_green_bag = [
    '4_dark_red_bag', '1_striped_white_bag', '3_faded_beige_bag',
    '5_wavy_red_bag'
]
shiny_purple_bag = [
    '1_clear_blue_bag', '4_striped_chartreuse_bag', '5_dark_maroon_bag'
]
dim_white_bag = [
    '3_striped_gold_bag', '4_striped_beige_bag', '2_muted_blue_bag',
    '4_muted_white_bag'
]
posh_maroon_bag = ['2_dotted_red_bag', '5_dotted_crimson_bag']
posh_chartreuse_bag = [
    '4_shiny_turquoise_bag', '5_posh_gray_bag', '2_mirrored_blue_bag',
    '5_light_maroon_bag'
]
dim_orange_bag = ['1_faded_beige_bag']
clear_gray_bag = [
    '1_bright_red_bag', '2_dull_cyan_bag', '3_bright_maroon_bag',
    '3_muted_gold_bag'
]
dull_purple_bag = ['4_muted_gold_bag', '2_faded_beige_bag']
muted_olive_bag = [
    '4_clear_blue_bag', '1_posh_lavender_bag', '1_posh_brown_bag',
    '2_striped_chartreuse_bag'
]
pale_lavender_bag = ['1_dull_gray_bag', '3_posh_silver_bag', '3_dark_aqua_bag']
shiny_blue_bag = ['5_bright_tan_bag', '4_faded_yellow_bag']
plaid_salmon_bag = ['3_shiny_teal_bag']
mirrored_silver_bag = ['4_plaid_tomato_bag', '5_dotted_salmon_bag']
light_blue_bag = [
    '3_pale_tan_bag', '2_mirrored_fuchsia_bag', '4_drab_maroon_bag',
    '1_posh_silver_bag'
]
light_orange_bag = ['2_dark_gold_bag', '1_dim_gold_bag']
faded_tomato_bag = ['2_wavy_beige_bag']
shiny_lime_bag = ['no_other_bag']
shiny_fuchsia_bag = [
    '5_muted_orange_bag', '2_shiny_plum_bag', '1_plaid_turquoise_bag'
]
light_indigo_bag = [
    '2_dim_purple_bag', '4_faded_magenta_bag', '3_dim_black_bag'
]
faded_aqua_bag = [
    '2_drab_beige_bag', '3_bright_aqua_bag', '3_drab_plum_bag',
    '2_dotted_silver_bag'
]
posh_blue_bag = ['1_wavy_magenta_bag', '5_posh_magenta_bag']
dotted_crimson_bag = ['3_striped_gold_bag', '3_dark_yellow_bag']
striped_salmon_bag = [
    '1_dark_tomato_bag', '5_shiny_coral_bag', '5_plaid_silver_bag'
]
clear_brown_bag = ['2_muted_olive_bag', '5_plaid_gold_bag']
clear_orange_bag = [
    '5_posh_plum_bag', '1_posh_lavender_bag', '3_dull_cyan_bag'
]
shiny_teal_bag = ['4_muted_gold_bag', '3_striped_chartreuse_bag']
dim_bronze_bag = ['4_dull_lavender_bag']
shiny_silver_bag = [
    '3_dull_plum_bag', '5_vibrant_indigo_bag', '4_striped_bronze_bag',
    '4_posh_tomato_bag'
]
dim_tomato_bag = ['5_wavy_indigo_bag', '3_wavy_gold_bag', '5_dim_beige_bag']
vibrant_white_bag = [
    '5_dim_magenta_bag', '2_posh_silver_bag', '5_dull_maroon_bag'
]
dark_blue_bag = [
    '4_striped_green_bag', '4_dotted_violet_bag', '4_bright_red_bag'
]
plaid_gray_bag = ['4_faded_gray_bag', '3_dark_brown_bag']
mirrored_indigo_bag = ['3_dim_crimson_bag']
mirrored_cyan_bag = [
    '5_faded_teal_bag', '4_striped_tan_bag', '3_bright_fuchsia_bag',
    '3_striped_bronze_bag'
]
dotted_red_bag = [
    '5_muted_olive_bag', '1_posh_lavender_bag', '2_faded_maroon_bag',
    '3_bright_tomato_bag'
]
clear_crimson_bag = ['4_muted_aqua_bag', '2_dark_lavender_bag']
mirrored_brown_bag = [
    '3_drab_beige_bag', '5_striped_lavender_bag', '4_dark_red_bag',
    '4_faded_brown_bag'
]
pale_gray_bag = [
    '4_vibrant_brown_bag', '5_dark_chartreuse_bag', '3_vibrant_gold_bag',
    '2_striped_tan_bag'
]
bright_gray_bag = [
    '2_dull_chartreuse_bag', '1_dull_purple_bag', '3_dotted_violet_bag'
]
dotted_purple_bag = [
    '5_shiny_silver_bag', '2_mirrored_white_bag', '3_shiny_indigo_bag'
]
dotted_indigo_bag = [
    '3_bright_gray_bag', '2_light_tomato_bag', '4_dim_violet_bag',
    '3_dull_chartreuse_bag'
]
wavy_orange_bag = [
    '4_muted_maroon_bag', '5_clear_salmon_bag', '5_dark_orange_bag'
]
dark_plum_bag = [
    '2_muted_tomato_bag', '3_shiny_gold_bag', '4_striped_chartreuse_bag'
]
vibrant_yellow_bag = [
    '5_dark_red_bag', '4_shiny_gold_bag', '3_light_silver_bag',
    '2_faded_yellow_bag'
]
vibrant_bronze_bag = ['5_clear_blue_bag']
striped_silver_bag = ['4_faded_cyan_bag', '5_posh_fuchsia_bag']
dull_yellow_bag = [
    '4_shiny_silver_bag', '2_posh_maroon_bag', '1_mirrored_lavender_bag',
    '2_dull_lavender_bag'
]
wavy_turquoise_bag = ['4_muted_gold_bag']
drab_salmon_bag = [
    '4_dotted_yellow_bag', '4_posh_aqua_bag', '1_dull_beige_bag'
]
posh_green_bag = [
    '5_mirrored_lavender_bag', '5_dim_maroon_bag', '2_faded_gray_bag',
    '1_wavy_lavender_bag'
]
muted_gold_bag = ['no_other_bag']
mirrored_aqua_bag = [
    '4_posh_olive_bag', '5_shiny_bronze_bag', '4_drab_blue_bag'
]
wavy_tan_bag = ['2_wavy_green_bag', '5_faded_brown_bag']
mirrored_magenta_bag = ['1_plaid_black_bag', '1_clear_violet_bag']
mirrored_lime_bag = [
    '1_clear_cyan_bag', '3_pale_maroon_bag', '5_striped_teal_bag'
]
dark_crimson_bag = [
    '2_vibrant_black_bag', '4_clear_violet_bag', '2_vibrant_indigo_bag'
]
striped_blue_bag = [
    '4_vibrant_cyan_bag', '3_striped_chartreuse_bag', '4_bright_tan_bag',
    '2_dull_lime_bag'
]
wavy_chartreuse_bag = [
    '4_dotted_silver_bag', '3_drab_red_bag', '5_posh_olive_bag'
]
clear_magenta_bag = ['3_clear_orange_bag', '1_plaid_plum_bag']
dim_beige_bag = [
    '3_vibrant_maroon_bag', '2_shiny_silver_bag', '4_faded_lavender_bag'
]
striped_tan_bag = ['5_mirrored_olive_bag', '4_dark_maroon_bag']
faded_green_bag = ['1_posh_white_bag', '1_dotted_crimson_bag']
drab_teal_bag = ['4_bright_fuchsia_bag']
posh_lavender_bag = [
    '3_bright_red_bag', '2_shiny_lime_bag', '2_bright_chartreuse_bag'
]
bright_tan_bag = ['5_clear_blue_bag', '2_dark_red_bag', '3_bright_maroon_bag']
light_red_bag = [
    '5_mirrored_plum_bag', '3_vibrant_black_bag', '5_vibrant_gray_bag'
]
light_white_bag = ['2_drab_beige_bag']
faded_gray_bag = ['5_dim_plum_bag', '1_bright_aqua_bag']
light_gray_bag = [
    '3_dark_plum_bag', '2_vibrant_silver_bag', '1_faded_gold_bag'
]
light_teal_bag = ['5_dark_lavender_bag']
muted_teal_bag = [
    '4_striped_chartreuse_bag', '2_muted_gold_bag', '1_mirrored_green_bag',
    '5_dull_orange_bag'
]
dull_chartreuse_bag = [
    '5_wavy_maroon_bag', '5_posh_black_bag', '1_shiny_purple_bag',
    '2_bright_tan_bag'
]
vibrant_salmon_bag = ['3_faded_beige_bag', '1_faded_magenta_bag']
mirrored_gold_bag = ['2_dark_orange_bag']
dark_yellow_bag = [
    '1_plaid_brown_bag', '3_dull_lime_bag', '4_shiny_gold_bag',
    '4_drab_beige_bag'
]
plaid_crimson_bag = ['4_pale_chartreuse_bag', '3_vibrant_indigo_bag']
shiny_gold_bag = ['1_muted_olive_bag', '5_dotted_red_bag', '1_drab_plum_bag']
pale_olive_bag = ['4_dark_maroon_bag', '1_clear_red_bag']
dotted_magenta_bag = ['2_dark_purple_bag']
striped_violet_bag = [
    '5_plaid_salmon_bag', '4_mirrored_cyan_bag', '2_faded_crimson_bag',
    '3_mirrored_fuchsia_bag'
]
faded_lime_bag = ['2_vibrant_brown_bag', '1_dim_purple_bag']
muted_magenta_bag = [
    '4_wavy_tomato_bag', '2_plaid_black_bag', '5_mirrored_olive_bag',
    '2_muted_turquoise_bag'
]
dim_lime_bag = ['1_wavy_beige_bag', '2_light_olive_bag']
plaid_cyan_bag = ['3_muted_yellow_bag']
dotted_maroon_bag = ['3_vibrant_green_bag', '2_light_purple_bag']
striped_gray_bag = ['3_plaid_tomato_bag']
light_violet_bag = [
    '2_striped_tomato_bag', '1_mirrored_beige_bag', '4_clear_magenta_bag',
    '3_muted_red_bag'
]
vibrant_gold_bag = [
    '2_striped_blue_bag', '4_dull_orange_bag', '2_striped_fuchsia_bag'
]
vibrant_lavender_bag = ['2_bright_red_bag', '3_dull_chartreuse_bag']
clear_yellow_bag = ['2_clear_orange_bag']
muted_black_bag = [
    '2_wavy_beige_bag', '3_light_magenta_bag', '5_plaid_chartreuse_bag'
]
pale_brown_bag = ['5_wavy_red_bag', '4_vibrant_red_bag']
plaid_purple_bag = ['4_dotted_violet_bag', '1_muted_white_bag']
vibrant_fuchsia_bag = ['3_mirrored_silver_bag']
light_purple_bag = [
    '3_light_green_bag', '4_wavy_lime_bag', '5_striped_chartreuse_bag',
    '4_shiny_blue_bag'
]
mirrored_white_bag = ['4_bright_brown_bag', '2_striped_silver_bag']
dull_silver_bag = ['5_shiny_gray_bag']
dark_magenta_bag = ['1_light_turquoise_bag', '4_plaid_brown_bag']
faded_red_bag = ['2_striped_tan_bag']
mirrored_beige_bag = [
    '4_clear_yellow_bag', '3_mirrored_orange_bag', '1_posh_lavender_bag'
]
faded_coral_bag = [
    '1_striped_blue_bag', '2_shiny_purple_bag', '5_muted_purple_bag'
]
shiny_cyan_bag = [
    '3_clear_purple_bag', '2_dim_orange_bag', '1_dark_teal_bag',
    '4_mirrored_chartreuse_bag'
]
posh_gray_bag = ['3_bright_red_bag', '3_faded_maroon_bag']
dim_cyan_bag = ['5_light_white_bag']
dotted_tomato_bag = ['5_plaid_lime_bag', '4_shiny_plum_bag', '1_wavy_blue_bag']
dark_teal_bag = ['4_shiny_turquoise_bag', '5_faded_green_bag']
muted_cyan_bag = [
    '2_bright_maroon_bag', '1_posh_coral_bag', '3_light_bronze_bag',
    '1_dim_tomato_bag'
]
dotted_yellow_bag = [
    '3_bright_maroon_bag', '4_dim_lime_bag', '3_faded_aqua_bag',
    '2_plaid_magenta_bag'
]
dark_cyan_bag = ['4_faded_beige_bag']
dark_bronze_bag = [
    '1_pale_white_bag', '4_shiny_chartreuse_bag', '1_vibrant_cyan_bag',
    '1_muted_yellow_bag'
]
drab_cyan_bag = ['5_clear_blue_bag', '4_bright_tan_bag', '5_wavy_red_bag']
drab_white_bag = ['5_shiny_yellow_bag']
bright_cyan_bag = [
    '3_bright_brown_bag', '2_clear_gold_bag', '4_striped_white_bag',
    '3_dark_yellow_bag'
]
dull_lavender_bag = ['4_mirrored_brown_bag', '4_pale_salmon_bag']
shiny_olive_bag = ['1_plaid_beige_bag']
posh_fuchsia_bag = ['5_posh_gray_bag']
plaid_aqua_bag = [
    '4_faded_turquoise_bag', '4_striped_silver_bag', '4_shiny_beige_bag',
    '3_dark_cyan_bag'
]
shiny_plum_bag = ['3_dull_tomato_bag']
striped_chartreuse_bag = [
    '4_posh_black_bag', '1_vibrant_cyan_bag', '2_bright_chartreuse_bag'
]
pale_red_bag = [
    '2_vibrant_bronze_bag', '3_posh_black_bag', '4_bright_tomato_bag'
]
plaid_maroon_bag = [
    '2_dotted_coral_bag', '4_wavy_tomato_bag', '3_pale_blue_bag'
]
shiny_beige_bag = ['4_faded_aqua_bag']
plaid_silver_bag = ['2_light_gold_bag', '2_wavy_green_bag', '4_posh_cyan_bag']
light_cyan_bag = ['5_shiny_tomato_bag', '1_wavy_magenta_bag']
faded_silver_bag = [
    '4_striped_bronze_bag', '3_pale_coral_bag', '2_dim_salmon_bag'
]
light_green_bag = ['5_vibrant_maroon_bag', '3_muted_indigo_bag']
faded_maroon_bag = [
    '5_dull_lime_bag', '1_plaid_black_bag', '5_drab_beige_bag',
    '5_clear_gray_bag'
]
posh_tan_bag = [
    '3_dim_violet_bag', '2_plaid_turquoise_bag', '4_pale_turquoise_bag',
    '1_dim_chartreuse_bag'
]
muted_silver_bag = ['3_muted_brown_bag', '2_dotted_crimson_bag']
mirrored_turquoise_bag = [
    '4_bright_cyan_bag', '1_light_turquoise_bag', '4_dark_silver_bag',
    '3_light_coral_bag'
]
clear_coral_bag = [
    '2_clear_gray_bag', '3_posh_plum_bag', '4_muted_indigo_bag',
    '3_pale_chartreuse_bag'
]
clear_teal_bag = ['2_light_turquoise_bag', '1_striped_white_bag']
muted_lavender_bag = [
    '5_posh_brown_bag', '3_striped_blue_bag', '3_clear_blue_bag'
]
shiny_tan_bag = ['1_light_olive_bag']
dark_salmon_bag = ['2_dull_teal_bag', '1_muted_aqua_bag', '5_dark_crimson_bag']
plaid_orange_bag = [
    '3_dull_plum_bag', '5_dim_maroon_bag', '2_faded_maroon_bag'
]
clear_black_bag = [
    '5_shiny_beige_bag', '1_plaid_tomato_bag', '2_dull_magenta_bag'
]
bright_red_bag = ['no_other_bag']
striped_tomato_bag = [
    '5_posh_lavender_bag', '2_dark_teal_bag', '2_drab_bronze_bag',
    '2_drab_chartreuse_bag'
]
light_maroon_bag = ['1_faded_magenta_bag', '4_mirrored_chartreuse_bag']
dark_indigo_bag = [
    '5_striped_purple_bag', '1_clear_tomato_bag', '4_light_beige_bag'
]
faded_violet_bag = ['1_striped_tan_bag']
clear_violet_bag = ['1_plaid_tan_bag', '2_light_salmon_bag']
dotted_violet_bag = ['4_light_silver_bag']
dotted_brown_bag = ['3_dim_gold_bag', '3_drab_chartreuse_bag']
wavy_gray_bag = ['2_drab_tan_bag']
faded_black_bag = ['1_faded_aqua_bag', '3_bright_gray_bag']
shiny_bronze_bag = [
    '4_muted_salmon_bag', '5_plaid_lime_bag', '1_faded_maroon_bag',
    '3_mirrored_silver_bag'
]
faded_purple_bag = ['3_wavy_beige_bag', '5_shiny_silver_bag']
dim_plum_bag = ['5_light_salmon_bag', '4_plaid_plum_bag', '2_posh_crimson_bag']
plaid_turquoise_bag = ['1_bright_purple_bag', '5_muted_tomato_bag']
clear_tomato_bag = ['2_striped_bronze_bag']
bright_green_bag = [
    '3_plaid_chartreuse_bag', '5_dim_orange_bag', '4_dull_magenta_bag'
]
drab_tomato_bag = ['5_wavy_tomato_bag', '5_posh_gold_bag']
clear_indigo_bag = ['1_posh_white_bag', '5_drab_plum_bag']
bright_crimson_bag = ['4_faded_salmon_bag']
dark_coral_bag = ['3_clear_indigo_bag', '5_dull_cyan_bag', '5_faded_teal_bag']
light_salmon_bag = ['2_muted_salmon_bag', '3_posh_brown_bag']
dark_purple_bag = [
    '2_shiny_chartreuse_bag', '5_clear_cyan_bag', '4_striped_fuchsia_bag',
    '5_light_silver_bag'
]
dotted_beige_bag = [
    '5_muted_olive_bag', '2_vibrant_cyan_bag', '4_light_turquoise_bag'
]
muted_crimson_bag = ['5_drab_plum_bag']
wavy_gold_bag = [
    '5_faded_red_bag', '4_bright_purple_bag', '3_drab_plum_bag',
    '4_dotted_red_bag'
]
faded_crimson_bag = ['5_bright_maroon_bag']
shiny_chartreuse_bag = ['5_posh_black_bag', '1_clear_blue_bag']
dull_magenta_bag = ['5_vibrant_beige_bag', '2_dull_chartreuse_bag']
shiny_turquoise_bag = ['4_faded_teal_bag']
drab_aqua_bag = ['1_muted_white_bag', '1_wavy_beige_bag', '5_bright_cyan_bag']
dim_teal_bag = ['5_vibrant_silver_bag']
light_yellow_bag = [
    '3_dull_lime_bag', '1_dotted_red_bag', '3_pale_turquoise_bag',
    '4_clear_gold_bag'
]
striped_olive_bag = ['1_clear_teal_bag', '5_dim_violet_bag']
dark_green_bag = ['1_posh_black_bag', '3_striped_fuchsia_bag']
light_black_bag = [
    '2_clear_beige_bag', '5_mirrored_beige_bag', '2_pale_blue_bag'
]
dull_brown_bag = [
    '4_posh_tomato_bag', '2_faded_beige_bag', '4_bright_violet_bag'
]
shiny_green_bag = [
    '4_wavy_tomato_bag', '1_faded_teal_bag', '3_muted_maroon_bag',
    '2_striped_crimson_bag'
]
shiny_salmon_bag = [
    '1_clear_gray_bag', '3_light_gold_bag', '2_mirrored_green_bag'
]
clear_aqua_bag = [
    '5_striped_chartreuse_bag', '1_light_tomato_bag', '1_pale_bronze_bag'
]
wavy_beige_bag = [
    '4_muted_salmon_bag', '1_dark_bronze_bag', '4_plaid_yellow_bag'
]
plaid_yellow_bag = [
    '5_mirrored_cyan_bag', '1_vibrant_violet_bag', '3_vibrant_coral_bag',
    '5_dim_cyan_bag'
]
clear_beige_bag = ['5_bright_red_bag']
clear_lime_bag = [
    '2_vibrant_coral_bag', '5_dark_lavender_bag', '2_pale_teal_bag'
]
vibrant_beige_bag = [
    '1_bright_tomato_bag', '2_drab_red_bag', '4_mirrored_cyan_bag'
]
bright_yellow_bag = ['1_pale_beige_bag', '3_dim_lime_bag', '5_posh_white_bag']
plaid_plum_bag = [
    '1_light_salmon_bag', '5_faded_yellow_bag', '2_shiny_brown_bag'
]
plaid_green_bag = [
    '3_posh_plum_bag', '5_mirrored_violet_bag', '5_light_lavender_bag',
    '4_plaid_plum_bag'
]
dull_tan_bag = [
    '1_drab_white_bag', '1_vibrant_bronze_bag', '3_dotted_crimson_bag'
]
clear_bronze_bag = ['3_clear_gray_bag', '1_dim_beige_bag']
vibrant_crimson_bag = ['4_shiny_plum_bag', '4_vibrant_orange_bag']
vibrant_orange_bag = [
    '2_bright_tomato_bag', '3_shiny_indigo_bag', '2_dotted_turquoise_bag',
    '4_striped_tan_bag'
]
plaid_beige_bag = ['2_light_white_bag']
dull_indigo_bag = ['1_faded_salmon_bag', '3_vibrant_cyan_bag']
muted_white_bag = ['4_striped_fuchsia_bag']
shiny_aqua_bag = [
    '1_shiny_teal_bag', '4_wavy_cyan_bag', '2_dark_green_bag',
    '4_bright_aqua_bag'
]
bright_fuchsia_bag = ['3_shiny_chartreuse_bag', '5_vibrant_bronze_bag']
dull_bronze_bag = [
    '5_drab_fuchsia_bag', '3_pale_beige_bag', '2_posh_lavender_bag'
]
muted_maroon_bag = [
    '2_posh_fuchsia_bag', '1_drab_plum_bag', '1_shiny_orange_bag'
]
striped_fuchsia_bag = [
    '4_posh_lavender_bag', '5_dull_cyan_bag', '2_posh_black_bag',
    '2_vibrant_bronze_bag'
]
shiny_tomato_bag = ['5_pale_violet_bag']
wavy_lime_bag = ['5_bright_red_bag', '2_bright_brown_bag', '1_dark_olive_bag']
wavy_tomato_bag = [
    '1_drab_tan_bag', '1_bright_maroon_bag', '3_mirrored_fuchsia_bag'
]
striped_coral_bag = ['2_pale_plum_bag', '5_muted_maroon_bag']
clear_silver_bag = ['2_striped_turquoise_bag']
vibrant_tomato_bag = [
    '4_drab_lime_bag', '3_dim_coral_bag', '3_mirrored_tan_bag'
]
faded_gold_bag = ['4_dull_black_bag']
striped_bronze_bag = [
    '5_dark_red_bag', '2_light_lavender_bag', '5_muted_olive_bag',
    '4_posh_gray_bag'
]
dotted_chartreuse_bag = [
    '2_dull_brown_bag', '4_dim_red_bag', '3_drab_beige_bag'
]
vibrant_coral_bag = ['3_shiny_turquoise_bag', '1_striped_orange_bag']
faded_lavender_bag = ['5_shiny_lime_bag']
dull_turquoise_bag = [
    '2_dark_olive_bag', '3_dark_coral_bag', '3_shiny_purple_bag',
    '3_clear_turquoise_bag'
]
shiny_yellow_bag = [
    '4_dim_gold_bag', '4_vibrant_silver_bag', '1_dark_yellow_bag'
]
plaid_lavender_bag = [
    '4_vibrant_violet_bag', '3_striped_silver_bag', '2_muted_crimson_bag',
    '1_light_tan_bag'
]
mirrored_fuchsia_bag = ['3_clear_gray_bag']
wavy_white_bag = ['3_dim_turquoise_bag']
clear_purple_bag = ['1_shiny_chartreuse_bag']
dark_chartreuse_bag = [
    '1_dim_blue_bag', '2_dark_maroon_bag', '1_light_lavender_bag',
    '1_drab_black_bag'
]
wavy_purple_bag = [
    '2_vibrant_brown_bag', '3_faded_olive_bag', '5_dim_gold_bag',
    '1_dull_brown_bag'
]
bright_lavender_bag = ['1_muted_white_bag']
shiny_red_bag = ['4_muted_aqua_bag', '5_striped_teal_bag', '1_dark_violet_bag']
pale_aqua_bag = ['3_dark_teal_bag', '3_dull_violet_bag']
wavy_brown_bag = [
    '4_posh_brown_bag', '3_posh_crimson_bag', '4_mirrored_lavender_bag'
]
clear_chartreuse_bag = ['2_bright_tan_bag']
mirrored_chartreuse_bag = [
    '5_plaid_black_bag', '3_dark_turquoise_bag', '2_posh_maroon_bag',
    '4_striped_silver_bag'
]
pale_turquoise_bag = [
    '2_dark_red_bag', '3_plaid_white_bag', '5_faded_tomato_bag',
    '4_dim_coral_bag'
]
dotted_blue_bag = ['4_bright_lavender_bag']
bright_plum_bag = [
    '5_plaid_salmon_bag', '1_dark_purple_bag', '2_muted_violet_bag',
    '3_dark_olive_bag'
]
pale_black_bag = ['1_dark_plum_bag']
dotted_coral_bag = [
    '4_muted_magenta_bag', '2_faded_magenta_bag', '1_clear_brown_bag'
]
plaid_magenta_bag = [
    '2_light_green_bag', '2_vibrant_coral_bag', '2_faded_beige_bag',
    '1_dim_teal_bag'
]
striped_lavender_bag = [
    '4_clear_gray_bag', '3_muted_teal_bag', '5_drab_beige_bag',
    '1_striped_bronze_bag'
]
striped_magenta_bag = [
    '3_dull_fuchsia_bag', '2_posh_olive_bag', '5_shiny_coral_bag',
    '1_dull_tan_bag'
]
pale_tan_bag = ['1_pale_olive_bag', '4_mirrored_teal_bag']
light_crimson_bag = ['4_dull_purple_bag']
pale_coral_bag = ['4_dotted_red_bag', '1_plaid_salmon_bag']
vibrant_blue_bag = [
    '5_shiny_yellow_bag', '2_drab_silver_bag', '1_faded_black_bag',
    '1_faded_lime_bag'
]
dark_tan_bag = [
    '1_shiny_brown_bag', '4_dark_green_bag', '3_drab_blue_bag',
    '4_drab_tan_bag'
]
drab_olive_bag = ['5_vibrant_yellow_bag']
wavy_violet_bag = ['5_shiny_coral_bag']
plaid_gold_bag = ['1_pale_salmon_bag', '4_plaid_beige_bag']
plaid_bronze_bag = [
    '5_bright_blue_bag', '1_wavy_green_bag', '3_clear_magenta_bag'
]
wavy_cyan_bag = ['2_clear_red_bag', '5_clear_indigo_bag']
vibrant_black_bag = ['2_mirrored_green_bag']
faded_white_bag = [
    '4_light_green_bag', '4_vibrant_teal_bag', '5_wavy_black_bag'
]
mirrored_orange_bag = ['4_muted_tomato_bag']
dark_gold_bag = [
    '1_muted_turquoise_bag', '4_mirrored_olive_bag', '2_dim_maroon_bag',
    '1_posh_olive_bag'
]
muted_turquoise_bag = ['1_plaid_tomato_bag']
dull_blue_bag = [
    '1_dotted_silver_bag', '2_vibrant_beige_bag', '3_muted_salmon_bag',
    '2_faded_teal_bag'
]
light_tomato_bag = ['4_dark_maroon_bag', '2_pale_red_bag', '4_dark_red_bag']
striped_turquoise_bag = [
    '5_dull_cyan_bag', '4_bright_violet_bag', '2_faded_violet_bag',
    '5_posh_silver_bag'
]
wavy_magenta_bag = [
    '1_muted_indigo_bag', '5_bright_brown_bag', '5_striped_tan_bag'
]
posh_bronze_bag = [
    '1_striped_fuchsia_bag', '5_dotted_salmon_bag', '3_striped_bronze_bag'
]
drab_silver_bag = ['2_plaid_white_bag', '2_plaid_lime_bag']
bright_maroon_bag = ['no_other_bag']
dull_red_bag = [
    '5_wavy_blue_bag', '3_light_green_bag', '4_mirrored_plum_bag',
    '3_mirrored_purple_bag'
]
pale_gold_bag = ['3_drab_plum_bag', '5_light_salmon_bag']
wavy_red_bag = ['4_light_lavender_bag', '5_drab_beige_bag']
mirrored_gray_bag = ['3_drab_white_bag', '1_posh_brown_bag']
drab_plum_bag = [
    '5_vibrant_bronze_bag', '1_muted_olive_bag', '1_striped_tan_bag'
]
mirrored_teal_bag = ['5_plaid_brown_bag', '3_plaid_salmon_bag']
dotted_tan_bag = [
    '3_drab_lavender_bag', '1_dark_bronze_bag', '5_vibrant_indigo_bag',
    '1_muted_purple_bag'
]
dark_gray_bag = [
    '5_vibrant_yellow_bag', '4_posh_lavender_bag', '1_drab_olive_bag',
    '1_dark_lavender_bag'
]
pale_indigo_bag = ['4_mirrored_silver_bag']
bright_white_bag = ['4_clear_magenta_bag']
clear_white_bag = ['4_faded_olive_bag']
faded_tan_bag = [
    '1_wavy_tomato_bag', '3_bright_cyan_bag', '4_drab_beige_bag',
    '3_striped_turquoise_bag'
]
striped_lime_bag = ['3_dim_lime_bag', '1_light_orange_bag']
dim_blue_bag = ['3_bright_maroon_bag']
mirrored_tomato_bag = ['3_plaid_silver_bag']
wavy_coral_bag = ['4_wavy_yellow_bag', '4_faded_white_bag']
dark_silver_bag = [
    '4_clear_cyan_bag', '3_vibrant_yellow_bag', '2_posh_gray_bag',
    '2_shiny_gold_bag'
]
dim_fuchsia_bag = [
    '3_plaid_orange_bag', '2_wavy_chartreuse_bag', '3_pale_chartreuse_bag'
]
light_lime_bag = [
    '2_striped_brown_bag', '3_muted_red_bag', '1_posh_crimson_bag',
    '5_bright_green_bag'
]
mirrored_red_bag = ['4_wavy_beige_bag', '5_dim_turquoise_bag']
light_chartreuse_bag = ['4_wavy_yellow_bag', '2_light_yellow_bag']
dull_teal_bag = ['4_dotted_gold_bag', '4_faded_maroon_bag']
dull_aqua_bag = ['4_dull_purple_bag', '2_light_lavender_bag']
pale_white_bag = ['3_pale_maroon_bag']
wavy_salmon_bag = [
    '4_posh_brown_bag', '1_light_brown_bag', '5_light_orange_bag',
    '3_dotted_olive_bag'
]
faded_chartreuse_bag = [
    '4_bright_tan_bag', '4_mirrored_silver_bag', '4_dotted_maroon_bag',
    '5_dark_beige_bag'
]
posh_beige_bag = ['4_dim_teal_bag']
posh_crimson_bag = [
    '5_dark_silver_bag', '4_vibrant_yellow_bag', '1_posh_gray_bag'
]
shiny_orange_bag = [
    '3_vibrant_cyan_bag', '1_wavy_red_bag', '3_bright_chartreuse_bag',
    '2_striped_tan_bag'
]
wavy_lavender_bag = [
    '1_dim_gold_bag', '4_clear_blue_bag', '1_plaid_crimson_bag',
    '3_faded_magenta_bag'
]
vibrant_aqua_bag = [
    '1_muted_black_bag', '5_pale_lavender_bag', '3_dim_cyan_bag'
]
dim_magenta_bag = ['2_dark_salmon_bag', '1_dark_orange_bag']
wavy_olive_bag = ['3_shiny_olive_bag', '2_bright_silver_bag']
dull_green_bag = [
    '3_drab_red_bag', '4_muted_turquoise_bag', '3_plaid_brown_bag',
    '4_mirrored_olive_bag'
]
dotted_gray_bag = ['5_vibrant_olive_bag', '4_drab_fuchsia_bag']
mirrored_salmon_bag = ['5_faded_indigo_bag', '5_vibrant_indigo_bag']
faded_orange_bag = ['5_striped_brown_bag', '5_muted_violet_bag']
plaid_black_bag = [
    '5_dark_green_bag', '4_bright_fuchsia_bag', '2_shiny_lime_bag'
]
dull_coral_bag = [
    '1_bright_tan_bag', '4_muted_salmon_bag', '1_bright_gray_bag'
]
pale_chartreuse_bag = [
    '4_faded_crimson_bag', '4_dotted_gold_bag', '4_posh_crimson_bag'
]
mirrored_black_bag = [
    '3_light_white_bag', '1_muted_magenta_bag', '1_mirrored_turquoise_bag',
    '4_bright_plum_bag'
]
drab_crimson_bag = ['1_light_tan_bag', '3_dull_green_bag', '1_wavy_blue_bag']
muted_orange_bag = ['5_dull_fuchsia_bag']
pale_orange_bag = ['4_vibrant_gray_bag']
clear_salmon_bag = ['3_clear_aqua_bag']
dull_tomato_bag = [
    '2_light_maroon_bag', '2_muted_lavender_bag', '1_muted_red_bag',
    '1_faded_brown_bag'
]
pale_crimson_bag = ['5_mirrored_chartreuse_bag']
dotted_white_bag = ['2_posh_brown_bag']
posh_teal_bag = ['4_dotted_salmon_bag', '1_dark_violet_bag']
dim_coral_bag = ['2_striped_white_bag']
bright_aqua_bag = [
    '4_bright_red_bag', '5_bright_tan_bag', '5_dotted_violet_bag'
]
dark_beige_bag = ['2_dull_aqua_bag', '2_drab_blue_bag']
bright_teal_bag = ['5_drab_white_bag']
dotted_silver_bag = ['3_dull_orange_bag']
striped_maroon_bag = [
    '4_drab_violet_bag', '2_light_black_bag', '4_light_lavender_bag'
]
pale_magenta_bag = ['4_pale_gray_bag']
shiny_maroon_bag = [
    '2_vibrant_beige_bag', '2_drab_lime_bag', '4_vibrant_turquoise_bag',
    '2_dull_chartreuse_bag'
]
dark_black_bag = [
    '1_dark_white_bag', '1_wavy_crimson_bag', '3_plaid_tan_bag',
    '5_striped_red_bag'
]
posh_white_bag = ['5_vibrant_gold_bag']
muted_aqua_bag = [
    '5_vibrant_gray_bag', '4_dull_chartreuse_bag', '3_bright_plum_bag',
    '1_dark_orange_bag'
]
pale_cyan_bag = ['3_muted_white_bag', '1_dark_olive_bag']
plaid_white_bag = [
    '4_plaid_black_bag', '4_light_white_bag', '3_plaid_salmon_bag'
]
bright_beige_bag = [
    '3_posh_magenta_bag', '2_clear_yellow_bag', '1_faded_plum_bag'
]
dotted_black_bag = ['1_muted_olive_bag']
bright_purple_bag = [
    '4_mirrored_cyan_bag', '1_faded_violet_bag', '1_dark_olive_bag'
]
faded_plum_bag = ['5_mirrored_olive_bag', '4_light_silver_bag']
dull_gold_bag = [
    '5_light_yellow_bag', '4_pale_gold_bag', '2_dotted_orange_bag'
]
dark_tomato_bag = ['4_muted_gold_bag', '3_shiny_gold_bag', '3_bright_red_bag']
pale_yellow_bag = [
    '4_drab_plum_bag', '1_clear_teal_bag', '4_faded_purple_bag',
    '2_posh_bronze_bag'
]
vibrant_turquoise_bag = [
    '3_dim_violet_bag', '2_muted_silver_bag', '3_plaid_cyan_bag',
    '3_faded_aqua_bag'
]
mirrored_coral_bag = [
    '2_posh_aqua_bag', '4_bright_violet_bag', '2_dark_salmon_bag'
]
muted_salmon_bag = ['1_vibrant_indigo_bag']
pale_plum_bag = [
    '5_mirrored_teal_bag', '1_drab_tan_bag', '3_plaid_crimson_bag'
]
clear_gold_bag = ['3_dull_cyan_bag', '3_plaid_brown_bag', '1_muted_tomato_bag']
muted_chartreuse_bag = ['4_posh_gray_bag', '5_drab_purple_bag']
light_coral_bag = ['4_clear_purple_bag', '5_drab_beige_bag']
faded_indigo_bag = ['1_dull_brown_bag']
bright_turquoise_bag = ['5_drab_bronze_bag']
clear_plum_bag = [
    '3_dark_red_bag', '3_dim_gold_bag', '2_posh_black_bag', '5_plaid_beige_bag'
]
plaid_chartreuse_bag = ['1_wavy_yellow_bag', '3_mirrored_olive_bag']
faded_bronze_bag = ['2_light_salmon_bag']
bright_lime_bag = [
    '3_faded_teal_bag', '5_dotted_coral_bag', '1_faded_crimson_bag'
]
drab_violet_bag = [
    '1_faded_beige_bag', '2_mirrored_chartreuse_bag', '2_clear_orange_bag',
    '4_dotted_beige_bag'
]
dull_olive_bag = ['5_muted_lime_bag', '3_dark_yellow_bag']
wavy_indigo_bag = ['1_clear_tan_bag', '5_vibrant_green_bag']
posh_indigo_bag = ['5_drab_salmon_bag']
dull_cyan_bag = ['no_other_bag']
plaid_brown_bag = [
    '5_striped_tan_bag', '2_dark_maroon_bag', '4_dim_chartreuse_bag',
    '3_dull_lime_bag'
]
mirrored_purple_bag = ['5_drab_green_bag', '2_clear_green_bag']
striped_plum_bag = ['5_dim_white_bag', '4_dark_teal_bag']
dim_lavender_bag = ['5_striped_bronze_bag', '3_wavy_maroon_bag']
dim_chartreuse_bag = ['3_shiny_gold_bag', '2_mirrored_olive_bag']

BAGS = [
    drab_tan_bag, vibrant_lime_bag, pale_lime_bag, dull_gray_bag,
    light_fuchsia_bag, drab_gold_bag, dim_red_bag, striped_orange_bag,
    shiny_violet_bag, faded_olive_bag, dotted_lime_bag, drab_magenta_bag,
    dull_black_bag, posh_turquoise_bag, muted_purple_bag, striped_black_bag,
    drab_brown_bag, pale_purple_bag, dark_turquoise_bag, clear_lavender_bag,
    bright_coral_bag, posh_coral_bag, drab_lime_bag, striped_brown_bag,
    wavy_bronze_bag, dim_black_bag, posh_yellow_bag, pale_violet_bag,
    mirrored_bronze_bag, vibrant_silver_bag, dark_brown_bag, wavy_green_bag,
    light_beige_bag, wavy_crimson_bag, clear_tan_bag, posh_lime_bag,
    pale_blue_bag, wavy_silver_bag, striped_beige_bag, dim_gold_bag,
    vibrant_teal_bag, light_tan_bag, dark_red_bag, posh_salmon_bag,
    mirrored_yellow_bag, dark_fuchsia_bag, bright_bronze_bag, posh_silver_bag,
    dotted_salmon_bag, dark_orange_bag, bright_silver_bag, posh_orange_bag,
    mirrored_olive_bag, drab_beige_bag, muted_bronze_bag, dark_lime_bag,
    dark_olive_bag, dull_white_bag, shiny_gray_bag, dotted_orange_bag,
    clear_olive_bag, drab_bronze_bag, drab_chartreuse_bag, faded_cyan_bag,
    plaid_fuchsia_bag, light_gold_bag, pale_bronze_bag, shiny_coral_bag,
    vibrant_green_bag, vibrant_violet_bag, muted_fuchsia_bag, bright_olive_bag,
    mirrored_maroon_bag, pale_salmon_bag, faded_brown_bag, dark_lavender_bag,
    plaid_coral_bag, drab_black_bag, shiny_black_bag, muted_plum_bag,
    shiny_lavender_bag, mirrored_blue_bag, dotted_aqua_bag, light_lavender_bag,
    bright_orange_bag, muted_tomato_bag, dim_indigo_bag, faded_turquoise_bag,
    wavy_teal_bag, dotted_bronze_bag, posh_purple_bag, dull_violet_bag,
    drab_indigo_bag, mirrored_crimson_bag, mirrored_tan_bag, wavy_fuchsia_bag,
    striped_yellow_bag, striped_white_bag, light_turquoise_bag, clear_blue_bag,
    faded_blue_bag, dim_aqua_bag, shiny_magenta_bag, wavy_maroon_bag,
    plaid_teal_bag, bright_tomato_bag, mirrored_lavender_bag,
    vibrant_purple_bag, posh_aqua_bag, faded_fuchsia_bag, dim_silver_bag,
    bright_brown_bag, dim_olive_bag, striped_teal_bag, posh_plum_bag,
    faded_teal_bag, striped_indigo_bag, drab_blue_bag, light_olive_bag,
    vibrant_red_bag, faded_salmon_bag, shiny_brown_bag, posh_olive_bag,
    clear_green_bag, mirrored_violet_bag, light_brown_bag, plaid_blue_bag,
    dim_green_bag, mirrored_plum_bag, dotted_turquoise_bag, dull_salmon_bag,
    wavy_plum_bag, bright_blue_bag, posh_tomato_bag, dotted_lavender_bag,
    posh_magenta_bag, faded_beige_bag, vibrant_plum_bag, pale_green_bag,
    dull_fuchsia_bag, light_plum_bag, dotted_olive_bag, striped_gold_bag,
    bright_violet_bag, dim_yellow_bag, bright_indigo_bag, plaid_lime_bag,
    striped_aqua_bag, dull_maroon_bag, muted_tan_bag, plaid_tan_bag,
    dull_beige_bag, posh_cyan_bag, drab_red_bag, drab_gray_bag, muted_red_bag,
    drab_green_bag, dim_gray_bag, dark_white_bag, posh_black_bag,
    dim_turquoise_bag, drab_lavender_bag, striped_crimson_bag,
    vibrant_olive_bag, dim_maroon_bag, muted_lime_bag, drab_purple_bag,
    muted_beige_bag, dotted_green_bag, bright_black_bag, wavy_yellow_bag,
    faded_yellow_bag, dim_purple_bag, bright_chartreuse_bag,
    vibrant_maroon_bag, pale_fuchsia_bag, dotted_teal_bag, dull_lime_bag,
    bright_salmon_bag, bright_magenta_bag, striped_red_bag, pale_teal_bag,
    clear_cyan_bag, muted_gray_bag, bright_gold_bag, clear_red_bag,
    striped_purple_bag, plaid_violet_bag, shiny_crimson_bag, posh_gold_bag,
    dim_crimson_bag, posh_red_bag, drab_turquoise_bag, vibrant_cyan_bag,
    light_bronze_bag, dotted_cyan_bag, drab_fuchsia_bag, clear_maroon_bag,
    dim_salmon_bag, wavy_aqua_bag, pale_beige_bag, dark_maroon_bag,
    light_aqua_bag, dim_tan_bag, vibrant_brown_bag, light_magenta_bag,
    clear_turquoise_bag, dull_crimson_bag, dull_orange_bag, wavy_black_bag,
    plaid_olive_bag, plaid_indigo_bag, dim_brown_bag, muted_indigo_bag,
    dull_plum_bag, vibrant_tan_bag, plaid_tomato_bag, shiny_white_bag,
    plaid_red_bag, drab_orange_bag, striped_green_bag, shiny_indigo_bag,
    drab_yellow_bag, faded_magenta_bag, muted_yellow_bag, posh_brown_bag,
    pale_tomato_bag, dark_aqua_bag, muted_blue_bag, light_silver_bag,
    muted_coral_bag, muted_green_bag, muted_brown_bag, dim_violet_bag,
    clear_fuchsia_bag, muted_violet_bag, posh_violet_bag, dark_violet_bag,
    dotted_fuchsia_bag, vibrant_indigo_bag, vibrant_gray_bag, dotted_plum_bag,
    vibrant_magenta_bag, drab_maroon_bag, dotted_gold_bag, striped_cyan_bag,
    pale_silver_bag, drab_coral_bag, vibrant_chartreuse_bag, pale_maroon_bag,
    wavy_blue_bag, mirrored_green_bag, shiny_purple_bag, dim_white_bag,
    posh_maroon_bag, posh_chartreuse_bag, dim_orange_bag, clear_gray_bag,
    dull_purple_bag, muted_olive_bag, pale_lavender_bag, shiny_blue_bag,
    plaid_salmon_bag, mirrored_silver_bag, light_blue_bag, light_orange_bag,
    faded_tomato_bag, shiny_lime_bag, shiny_fuchsia_bag, light_indigo_bag,
    faded_aqua_bag, posh_blue_bag, dotted_crimson_bag, striped_salmon_bag,
    clear_brown_bag, clear_orange_bag, shiny_teal_bag, dim_bronze_bag,
    shiny_silver_bag, dim_tomato_bag, vibrant_white_bag, dark_blue_bag,
    plaid_gray_bag, mirrored_indigo_bag, mirrored_cyan_bag, dotted_red_bag,
    clear_crimson_bag, mirrored_brown_bag, pale_gray_bag, bright_gray_bag,
    dotted_purple_bag, dotted_indigo_bag, wavy_orange_bag, dark_plum_bag,
    vibrant_yellow_bag, vibrant_bronze_bag, striped_silver_bag,
    dull_yellow_bag, wavy_turquoise_bag, drab_salmon_bag, posh_green_bag,
    muted_gold_bag, mirrored_aqua_bag, wavy_tan_bag, mirrored_magenta_bag,
    mirrored_lime_bag, dark_crimson_bag, striped_blue_bag, wavy_chartreuse_bag,
    clear_magenta_bag, dim_beige_bag, striped_tan_bag, faded_green_bag,
    drab_teal_bag, posh_lavender_bag, bright_tan_bag, light_red_bag,
    light_white_bag, faded_gray_bag, light_gray_bag, light_teal_bag,
    muted_teal_bag, dull_chartreuse_bag, vibrant_salmon_bag, mirrored_gold_bag,
    dark_yellow_bag, plaid_crimson_bag, shiny_gold_bag, pale_olive_bag,
    dotted_magenta_bag, striped_violet_bag, faded_lime_bag, muted_magenta_bag,
    dim_lime_bag, plaid_cyan_bag, dotted_maroon_bag, striped_gray_bag,
    light_violet_bag, vibrant_gold_bag, vibrant_lavender_bag, clear_yellow_bag,
    muted_black_bag, pale_brown_bag, plaid_purple_bag, vibrant_fuchsia_bag,
    light_purple_bag, mirrored_white_bag, dull_silver_bag, dark_magenta_bag,
    faded_red_bag, mirrored_beige_bag, faded_coral_bag, shiny_cyan_bag,
    posh_gray_bag, dim_cyan_bag, dotted_tomato_bag, dark_teal_bag,
    muted_cyan_bag, dotted_yellow_bag, dark_cyan_bag, dark_bronze_bag,
    drab_cyan_bag, drab_white_bag, bright_cyan_bag, dull_lavender_bag,
    shiny_olive_bag, posh_fuchsia_bag, plaid_aqua_bag, shiny_plum_bag,
    striped_chartreuse_bag, pale_red_bag, plaid_maroon_bag, shiny_beige_bag,
    plaid_silver_bag, light_cyan_bag, faded_silver_bag, light_green_bag,
    faded_maroon_bag, posh_tan_bag, muted_silver_bag, mirrored_turquoise_bag,
    clear_coral_bag, clear_teal_bag, muted_lavender_bag, shiny_tan_bag,
    dark_salmon_bag, plaid_orange_bag, clear_black_bag, bright_red_bag,
    striped_tomato_bag, light_maroon_bag, dark_indigo_bag, faded_violet_bag,
    clear_violet_bag, dotted_violet_bag, dotted_brown_bag, wavy_gray_bag,
    faded_black_bag, shiny_bronze_bag, faded_purple_bag, dim_plum_bag,
    plaid_turquoise_bag, clear_tomato_bag, bright_green_bag, drab_tomato_bag,
    clear_indigo_bag, bright_crimson_bag, dark_coral_bag, light_salmon_bag,
    dark_purple_bag, dotted_beige_bag, muted_crimson_bag, wavy_gold_bag,
    faded_crimson_bag, shiny_chartreuse_bag, dull_magenta_bag,
    shiny_turquoise_bag, drab_aqua_bag, dim_teal_bag, light_yellow_bag,
    striped_olive_bag, dark_green_bag, light_black_bag, dull_brown_bag,
    shiny_green_bag, shiny_salmon_bag, clear_aqua_bag, wavy_beige_bag,
    plaid_yellow_bag, clear_beige_bag, clear_lime_bag, vibrant_beige_bag,
    bright_yellow_bag, plaid_plum_bag, plaid_green_bag, dull_tan_bag,
    clear_bronze_bag, vibrant_crimson_bag, vibrant_orange_bag, plaid_beige_bag,
    dull_indigo_bag, muted_white_bag, shiny_aqua_bag, bright_fuchsia_bag,
    dull_bronze_bag, muted_maroon_bag, striped_fuchsia_bag, shiny_tomato_bag,
    wavy_lime_bag, wavy_tomato_bag, striped_coral_bag, clear_silver_bag,
    vibrant_tomato_bag, faded_gold_bag, striped_bronze_bag,
    dotted_chartreuse_bag, vibrant_coral_bag, faded_lavender_bag,
    dull_turquoise_bag, shiny_yellow_bag, plaid_lavender_bag,
    mirrored_fuchsia_bag, wavy_white_bag, clear_purple_bag,
    dark_chartreuse_bag, wavy_purple_bag, bright_lavender_bag, shiny_red_bag,
    pale_aqua_bag, wavy_brown_bag, clear_chartreuse_bag,
    mirrored_chartreuse_bag, pale_turquoise_bag, dotted_blue_bag,
    bright_plum_bag, pale_black_bag, dotted_coral_bag, plaid_magenta_bag,
    striped_lavender_bag, striped_magenta_bag, pale_tan_bag, light_crimson_bag,
    pale_coral_bag, vibrant_blue_bag, dark_tan_bag, drab_olive_bag,
    wavy_violet_bag, plaid_gold_bag, plaid_bronze_bag, wavy_cyan_bag,
    vibrant_black_bag, faded_white_bag, mirrored_orange_bag, dark_gold_bag,
    muted_turquoise_bag, dull_blue_bag, light_tomato_bag,
    striped_turquoise_bag, wavy_magenta_bag, posh_bronze_bag, drab_silver_bag,
    bright_maroon_bag, dull_red_bag, pale_gold_bag, wavy_red_bag,
    mirrored_gray_bag, drab_plum_bag, mirrored_teal_bag, dotted_tan_bag,
    dark_gray_bag, pale_indigo_bag, bright_white_bag, clear_white_bag,
    faded_tan_bag, striped_lime_bag, dim_blue_bag, mirrored_tomato_bag,
    wavy_coral_bag, dark_silver_bag, dim_fuchsia_bag, light_lime_bag,
    mirrored_red_bag, light_chartreuse_bag, dull_teal_bag, dull_aqua_bag,
    pale_white_bag, wavy_salmon_bag, faded_chartreuse_bag, posh_beige_bag,
    posh_crimson_bag, shiny_orange_bag, wavy_lavender_bag, vibrant_aqua_bag,
    dim_magenta_bag, wavy_olive_bag, dull_green_bag, dotted_gray_bag,
    mirrored_salmon_bag, faded_orange_bag, plaid_black_bag, dull_coral_bag,
    pale_chartreuse_bag, mirrored_black_bag, drab_crimson_bag,
    muted_orange_bag, pale_orange_bag, clear_salmon_bag, dull_tomato_bag,
    pale_crimson_bag, dotted_white_bag, posh_teal_bag, dim_coral_bag,
    bright_aqua_bag, dark_beige_bag, bright_teal_bag, dotted_silver_bag,
    striped_maroon_bag, pale_magenta_bag, shiny_maroon_bag, dark_black_bag,
    posh_white_bag, muted_aqua_bag, pale_cyan_bag, plaid_white_bag,
    bright_beige_bag, dotted_black_bag, bright_purple_bag, faded_plum_bag,
    dull_gold_bag, dark_tomato_bag, pale_yellow_bag, vibrant_turquoise_bag,
    mirrored_coral_bag, muted_salmon_bag, pale_plum_bag, clear_gold_bag,
    muted_chartreuse_bag, light_coral_bag, faded_indigo_bag,
    bright_turquoise_bag, clear_plum_bag, plaid_chartreuse_bag,
    faded_bronze_bag, bright_lime_bag, drab_violet_bag, dull_olive_bag,
    wavy_indigo_bag, posh_indigo_bag, dull_cyan_bag, plaid_brown_bag,
    mirrored_purple_bag, striped_plum_bag, dim_lavender_bag, dim_chartreuse_bag
]

####################################################
#                  PART ONE                        #
####################################################

RECURSIVE_COUNT = 0


def search_bags(bag):
    """Recursively search bags"""
    global RECURSIVE_COUNT
    for i in bag:
        bag_name = i[2:]
        if bag_name == 'shiny_gold_bag':
            RECURSIVE_COUNT += 1
        elif i != 'no_other_bag' and bag_name != 'shiny_gold_bag':
            search_bags(globals()[bag_name])
        elif i == 'no_other_bag':
            RECURSIVE_COUNT += 0


def part_one():
    """Part 1 solution"""
    global RECURSIVE_COUNT
    bag_count = 0
    for bag in BAGS:
        RECURSIVE_COUNT = 0
        search_bags(bag)
        if RECURSIVE_COUNT > 0:
            bag_count += 1
    print(f'Solution 1: {bag_count}')


part_one()

####################################################
#                  PART TWO                        #
####################################################

TOTAL_BAG_COUNT = 0


def search_bags_again(bag):
    """Recursively search bags"""
    global TOTAL_BAG_COUNT
    for i in bag:
        bag_name = i[2:]
        if i != 'no_other_bag':
            bag_number = int(i[0])
            for j in range(bag_number):
                TOTAL_BAG_COUNT += 1
                search_bags_again(globals()[bag_name])


def part_two():
    """Part 2 solution"""
    global TOTAL_BAG_COUNT
    search_bags_again(shiny_gold_bag)
    print(f'Solution 2: {TOTAL_BAG_COUNT}')


part_two()

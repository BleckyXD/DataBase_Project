import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mariadb import Cursor
import luisData as ld

def infoObtain(cursor: Cursor):
# ============================Query 1=============================
    query_gender = """
    SELECT 
        Channel_Used AS media_type,
        COUNT(*) AS consumer_count, 
        SUBSTRING_INDEX(Target_Audience,' ', 1) AS Gender
    FROM advertisingdata 
    WHERE Target_Audience != 'All Ages'
    GROUP BY Channel_Used, Target_Audience;
    """
    # Run query using the same cursor
    cursor.execute(query_gender)
    rows = cursor.fetchall()
    # Convert to DataFrame (same as before)
    ld.df_gender = pd.DataFrame(rows)

#============================Query 2=============================
    query_age = """
    SELECT
        Duration,
        SUBSTRING_INDEX(Target_Audience, ' ', -1) AS Age_Range,
        COUNT(*) AS consumer_count
    FROM advertisingdata
    WHERE Target_Audience NOT LIKE 'All Ages'
    GROUP BY Duration, Age_Range
    ORDER BY Duration, Age_Range;
    """
    cursor.execute(query_age)
    rows = cursor.fetchall()
    # Convert to DataFrame (same as before)
    ld.df_age = pd.DataFrame(rows)

#============================Query 3=============================
    query_segment = """
    SELECT
        Customer_Segment,
        Language,
        COUNT(*) AS consumer_count
    FROM advertisingdata
    GROUP BY Customer_Segment, Language
    ORDER BY Customer_Segment, Language;
    """
    cursor.execute(query_segment)
    rows = cursor.fetchall()
    # Convert to DataFrame (same as before)
    ld.df_segment = pd.DataFrame(rows)

#============================Query 4=============================
    query_clicks = """
    SELECT
        Location AS City,
        Duration,
        SUM(Clicks) AS total_clicks
    FROM advertisingdata
    GROUP BY Location, Duration
    ORDER BY Location, Duration;
    """
    cursor.execute(query_clicks)
    rows = cursor.fetchall()
    # Convert to DataFrame (same as before)
    ld.df_clicks = pd.DataFrame(rows)

#============================Query 5=============================
    query_goal_segment = """
    SELECT
        Campaign_Goal,
        Customer_Segment,
        COUNT(*) AS consumer_count
    FROM advertisingdata
    GROUP BY Campaign_Goal, Customer_Segment
    ORDER BY Campaign_Goal, Customer_Segment;
    """
    cursor.execute(query_goal_segment)
    rows = cursor.fetchall()
    # Convert to DataFrame (same as before)
    ld.df_goal_segment = pd.DataFrame(rows)


# ========================================================
# GRAPH 1: Distribution by Gender and Media Type
# ========================================================
def graph1():

    # === same graph code ===
    platforms = ld.df_gender['media_type'].unique()
    genders = ld.df_gender['Gender'].unique()

    data_gender = np.zeros((len(platforms), len(genders)))
    for i, platform in enumerate(platforms):
        for j, gender in enumerate(genders):
            value = ld.df_gender[(ld.df_gender['media_type'] == platform) &
                              (ld.df_gender['Gender'] == gender)]['consumer_count']
            data_gender[i, j] = int(value.values[0]) if not value.empty else 0

    fig1 = plt.figure(figsize=(12, 8))
    ax1 = fig1.add_subplot(projection='3d')

    x_pos = np.arange(len(platforms))
    y_pos = np.arange(len(genders))
    x_pos, y_pos = np.meshgrid(x_pos, y_pos)
    x_pos, y_pos = x_pos.flatten(), y_pos.flatten()
    z_pos = np.zeros_like(x_pos)
    heights = data_gender.T.flatten()
    dx = dy = 0.4

    colors = ['#0096FF', '#FF2D96']  # Men / Women
    bar_colors = [colors[j % len(colors)] for j in np.repeat(range(len(genders)), len(platforms))]

    ax1.bar3d(x_pos, y_pos, z_pos, dx, dy, heights, color=bar_colors, shade=True)

    # Add value labels
    for x, y, z, h in zip(x_pos, y_pos, z_pos, heights):
        if h > 0:
            ax1.text(x + dx/2, y + dy/2, h + (max(heights)*0.02),
                    f'{int(h)}', color='black', ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax1.set_xticks(np.arange(len(platforms)))
    ax1.set_xticklabels(platforms, rotation=45)
    ax1.set_yticks(np.arange(len(genders)))
    ax1.set_yticklabels(genders)
    ax1.set_zlabel('Number of Consumers', fontweight='bold')
    ax1.set_title('Distribution of Consumers by Gender and Media Type', fontweight='bold')
    ax1.ticklabel_format(axis='z', style='plain')  # remove 1e8
    plt.show()


#========================================================
# GRAPH 2: Age Distribution by Advertisement Duration
#========================================================
def graph2():
    durations = ld.df_age['Duration'].unique()
    ages = ld.df_age['Age_Range'].unique()

    data_age = np.zeros((len(durations), len(ages)))
    for i, dur in enumerate(durations):
        for j, age in enumerate(ages):
            value = ld.df_age[(ld.df_age['Duration'] == dur) & (ld.df_age['Age_Range'] == age)]['consumer_count']
            data_age[i, j] = int(value.values[0]) if not value.empty else 0

    fig2 = plt.figure(figsize=(12, 8))
    ax2 = fig2.add_subplot(projection='3d')

    x_pos = np.arange(len(durations))
    y_pos = np.arange(len(ages))
    x_pos, y_pos = np.meshgrid(x_pos, y_pos)
    x_pos, y_pos = x_pos.flatten(), y_pos.flatten()
    z_pos = np.zeros_like(x_pos)
    heights = data_age.T.flatten()
    dx = dy = 0.4

    age_colors = ['#FF7F50', '#FFD700', '#32CD32', '#1E90FF']
    bar_colors = [age_colors[j % len(age_colors)] for j in np.repeat(range(len(ages)), len(durations))]

    ax2.bar3d(x_pos, y_pos, z_pos, dx, dy, heights, color=bar_colors, shade=True)
    for x, y, z, h in zip(x_pos, y_pos, z_pos, heights):
        if h > 0:
            ax2.text(x + dx/2, y + dy/2, h + (max(heights)*0.02),
                     f'{int(h)}', color='black', ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax2.set_xticks(np.arange(len(durations)))
    ax2.set_xticklabels(durations, rotation=30)
    ax2.set_yticks(np.arange(len(ages)))
    ax2.set_yticklabels(ages)
    ax2.set_zlabel('Number of Consumers', fontweight='bold')
    ax2.set_title('Age Distribution of Consumers by Advertisement Duration', fontweight='bold')
    ax2.ticklabel_format(axis='z', style='plain')
    plt.show()


# ========================================================
# GRAPH 3: Amount of People by Customer Segment and Language
# ========================================================
def graph3():
    segments = ld.df_segment['Customer_Segment'].unique()
    languages = ld.df_segment['Language'].unique()

    data_segment = np.zeros((len(segments), len(languages)))
    for i, seg in enumerate(segments):
        for j, lang in enumerate(languages):
            value = ld.df_segment[(ld.df_segment['Customer_Segment'] == seg) &
                               (ld.df_segment['Language'] == lang)]['consumer_count']
            data_segment[i, j] = int(value.values[0]) if not value.empty else 0

    fig3 = plt.figure(figsize=(12, 8))
    ax3 = fig3.add_subplot(projection='3d')

    x_pos = np.arange(len(segments))
    y_pos = np.arange(len(languages))
    x_pos, y_pos = np.meshgrid(x_pos, y_pos)
    x_pos, y_pos = x_pos.flatten(), y_pos.flatten()
    z_pos = np.zeros_like(x_pos)
    heights = data_segment.T.flatten()
    dx = dy = 0.4

    colors = ['#1E90FF', '#FFD700', '#FF69B4']
    bar_colors = [colors[j % len(colors)] for j in np.repeat(range(len(languages)), len(segments))]

    ax3.bar3d(x_pos, y_pos, z_pos, dx, dy, heights, color=bar_colors, shade=True)
    for x, y, z, h in zip(x_pos, y_pos, z_pos, heights):
        if h > 0:
            ax3.text(x + dx/2, y + dy/2, h + (max(heights)*0.02),
                     f'{int(h)}', color='black', ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax3.set_xticks(np.arange(len(segments)))
    ax3.set_xticklabels(segments, rotation=45)
    ax3.set_yticks(np.arange(len(languages)))
    ax3.set_yticklabels(languages)
    ax3.set_zlabel('Number of Consumers', fontweight='bold')
    ax3.set_title('Amount of People by Customer Segment and Language', fontweight='bold')
    ax3.ticklabel_format(axis='z', style='plain')
    plt.show()


# ========================================================
# GRAPH 4: Amount of Clicks in Different Cities Based on Duration
# ========================================================
def graph4():
    cities = ld.df_clicks['City'].unique()
    durations = ld.df_clicks['Duration'].unique()

    data_clicks = np.zeros((len(cities), len(durations)))
    for i, city in enumerate(cities):
        for j, dur in enumerate(durations):
            value = ld.df_clicks[(ld.df_clicks['City'] == city) & (ld.df_clicks['Duration'] == dur)]['total_clicks']
            data_clicks[i, j] = int(value.values[0]) if not value.empty else 0

    fig4 = plt.figure(figsize=(12, 8))
    ax4 = fig4.add_subplot(projection='3d')

    x_pos = np.arange(len(cities))
    y_pos = np.arange(len(durations))
    x_pos, y_pos = np.meshgrid(x_pos, y_pos)
    x_pos, y_pos = x_pos.flatten(), y_pos.flatten()
    z_pos = np.zeros_like(x_pos)
    heights = data_clicks.T.flatten()
    dx = dy = 0.4

    colors = ['#1E90FF', '#FFD700', '#FF69B4']
    bar_colors = [colors[j % len(colors)] for j in np.repeat(range(len(durations)), len(cities))]

    ax4.bar3d(x_pos, y_pos, z_pos, dx, dy, heights, color=bar_colors, shade=True)
    for x, y, z, h in zip(x_pos, y_pos, z_pos, heights):
        if h > 0:
            ax4.text(x + dx/2, y + dy/2, h + (max(heights)*0.02),
                     f'{int(h)}', color='black', ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax4.set_xticks(np.arange(len(cities)))
    ax4.set_xticklabels(cities, rotation=45)
    ax4.set_yticks(np.arange(len(durations)))
    ax4.set_yticklabels(durations)
    ax4.set_zlabel('Total Clicks', fontweight='bold')
    ax4.set_title('Amount of Clicks in Different Cities Based on Duration', fontweight='bold')
    ax4.ticklabel_format(axis='z', style='plain')
    plt.show()

# ========================================================
# GRAPH 5: Amount of People per Campaign Goal and Customer Segment
# ========================================================
def graph5():
    goals = ld.df_goal_segment['Campaign_Goal'].unique()
    segments = ld.df_goal_segment['Customer_Segment'].unique()

    data_goal_segment = np.zeros((len(goals), len(segments)))
    for i, goal in enumerate(goals):
        for j, seg in enumerate(segments):
            value = ld.df_goal_segment[(ld.df_goal_segment['Campaign_Goal'] == goal) &
                                    (ld.df_goal_segment['Customer_Segment'] == seg)]['consumer_count']
            data_goal_segment[i, j] = int(value.values[0]) if not value.empty else 0

    fig5 = plt.figure(figsize=(12, 8))
    ax5 = fig5.add_subplot(projection='3d')

    x_pos = np.arange(len(goals))
    y_pos = np.arange(len(segments))
    x_pos, y_pos = np.meshgrid(x_pos, y_pos)
    x_pos, y_pos = x_pos.flatten(), y_pos.flatten()
    z_pos = np.zeros_like(x_pos)
    heights = data_goal_segment.T.flatten()
    dx = dy = 0.4

    colors = ['#FF7F50', '#FFD700', '#32CD32', '#1E90FF']
    bar_colors = [colors[j % len(colors)] for j in np.repeat(range(len(segments)), len(goals))]

    ax5.bar3d(x_pos, y_pos, z_pos, dx, dy, heights, color=bar_colors, shade=True)
    for x, y, z, h in zip(x_pos, y_pos, z_pos, heights):
        if h > 0:
            ax5.text(x + dx/2, y + dy/2, h + (max(heights)*0.02),
                     f'{int(h)}', color='black', ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax5.set_xticks(np.arange(len(goals)))
    ax5.set_xticklabels(goals, rotation=30)
    ax5.set_yticks(np.arange(len(segments)))
    ax5.set_yticklabels(segments)
    ax5.set_zlabel('Number of People', fontweight='bold')
    ax5.set_title('Amount of People per Campaign Goal and Customer Segment', fontweight='bold')
    ax5.ticklabel_format(axis='z', style='plain')
    plt.show()
import seaborn as sns


# Import data from shared.py
from shared import df, df2, df3, pd
from shiny.express import input, render, ui

# Page title (with some additional top padding)
ui.page_opts(title=ui.h2("Mariano's First NWSL Shiny app", class_="pt-5"))

 
# Render a scatterplot of the selected variable (input.var())
@render.plot
def scat1():
    p = sns.scatterplot(df, x=input.var(), y=input.var2(), edgecolor="white", hue= "Squad")
    sns.move_legend(p, "upper left", bbox_to_anchor=(.99,1))
    return p

ui.input_select("var", "Select expected assisted goals or minutes played for midfielders", choices=["xAG", "Min"])
ui.input_select("var2", "Select y variable for midfielders", choices=["HP", "PrgUsgAA", "tklintAA", "ShAA", "RecovAA", "Diff"])

@render.plot
def scat2():
    p = sns.scatterplot(df2, x=input.var3(), y=input.var4(), edgecolor="white", hue= "Squad")
    sns.move_legend(p, "upper left", bbox_to_anchor=(.99,1))
    return p

# Select input for choosing the variable to plot
ui.input_select("var3", "Select expected assisted goals or minutes played for defenders", choices=["xAG", "Min"])
ui.input_select("var4", "Select y variable for defenders", choices=["HP", "PrgUsgAA", "tklintAA", "ShAA", "RecovAA", "Diff"])

@render.plot
def scat3():
    p= sns.scatterplot(df3, x=input.var5(), y=input.var6(), edgecolor="white", hue= "Squad")
    sns.move_legend(p, "upper left", bbox_to_anchor=(.99,1))
    return p

ui.input_select("var5", "Select expected assisted goals or minutes played for forwards", choices=["xAG", "Min"])
ui.input_select("var6", "Select y variable for forwards", choices=["HP", "PrgUsgAA", "tklintAA", "ShAA", "RecovAA", "Diff"])

ui.input_select("var7", "Select to see table: Midfielder, Defender, or Forward", choices= ["MF", "DF", "FW"])

@render.table
def table():
    if input.var7() == "MF":
        return df
    elif input.var7() == "DF":
        return df2
    else:
        return df3
    

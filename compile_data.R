library(tidyverse)
library(readxl)
library(janitor)
library(textclean)

cnog <- data.frame(comment = read_lines("data/comments-not-on-github.txt")) %>% 
  mutate(comment = str_replace_all(comment, "\"", ""))

# May need work
csoec <- read_csv("data/community_survey_open_ended_comments_2016_2017_1_needswork.csv") %>% 
  select(comment)

dwsw <- read_excel("data/data.world set_goodstuffwoman.xlsx") %>% 
  clean_names() %>% 
  pivot_longer(c(team, empowerment, gender_groups, race_groups, gender_comp, race_comps, improvements), values_to = "comment") %>% 
  select(comment)

kpis <- read_csv("data/key-performance-indicator-surveys-1needswork.csv") %>% 
  clean_names() %>% 
  select(comment = additional_feedback) %>% 
  filter(!is.na(comment), nchar(comment) > 5)

sc <- read_csv("data/salaries_clean_ok.csv") %>% 
  select(comment = comments) %>% 
  filter(!is.na(comment))

training_comments <- bind_rows(cnog, csoec, dwsw, kpis, sc) %>% 
  mutate(comment = str_replace_all(comment, "\"", ""),
         comment = replace_non_ascii(comment, " "),
         comment = str_trunc(comment, 1000, "right", ellipsis = ""))
  
write_csv(training_comments, "data/training_comments.csv", col_names = FALSE)

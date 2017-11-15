#!/usr/bin/env ruby

# This is the Codecademy Daffy Duckifier program
# It replaces every occurence of the letter “s” with “th” and then presents the
# result to the user

#TODO:
# - Add an additional if statement to re-prompt the user for input if they don't
#   enter anything
# - Think about how you might account for words in which the letter “c” sounds
#   like an “s”
# - Think about how you might preserve the user's original capitalization

print "Thtring, pleathe!: "
user_input = gets.chomp
user_input.downcase!

if user_input.include? "s"
  user_input.gsub!(/s/, "th")
elsif user_input == ""
  print "Thtring, pleathe!: "
  user_input = gets.chomp
  user_input.downcase!
else
  puts "Nothing to do here!"
end

puts "Your string is: #{user_input}"

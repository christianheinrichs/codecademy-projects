#!/usr/bin/env ruby

#TODO:
# - What could you do to make sure your redactor redacts a word
#   regardless of whether it's upper case or lower case?
# - How could you make your program take multiple, separate words to REDACT?
# - How might you make a new redacted string and save it as a variable,
#   rather than just printing it to the console?

puts "Enter string here:"
text = gets.chomp

puts "Which word should be redacted?"
redact = gets.chomp

words = text.split(" ")

words.each do |word|
  if word == redact
    print "REDACTED "
  else
    print word + " "
  end
end

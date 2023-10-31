#!/usr/bin/env ruby

file = "text_messages.log"

File.open(file, "r") do |f|
  f.each_line do |line|
    match = line.match(/\[(.*?)\],\[(.*?)\]\(([^)]*)\)/

    if match
      sender = match[1]
      receiver = match[2]
      flags = match[3]

      puts "[#{sender}],[#{receiver}],[#{flags}]"
    end
  end
end

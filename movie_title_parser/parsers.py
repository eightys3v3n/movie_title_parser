import unittest
import os.path
import re


def remove_extension(name):
  pos = name.rfind(os.path.extsep)
  if pos == -1:
    return name
  name = name[0:pos]
  return name


def fix_word_seperators(name):
  name = name.replace('_', ' ')
  name = name.replace('.', ' ')
  return name


def remove_tags(name):
  name = re.sub(r"\(.*?\)", '', name)
  name = re.sub(r"\[.*?\]", '', name)
  return name


def remove_resolution(name):
  name = re.sub('[0-9]{3,4}x[0-9]{3,4}', '', name)
  name = re.sub('[0-9]{3,4}p', '', name)
  return name


def remove_keywords(name):
  keywords = [
    'x264',
    'yify',
    'h264',
    'bluray',
    'dvd',
    'aac',
    'brrip',
    'web-dl',
    'dts',
    'ac3',
    'webrip',
    'marvel',
  ]
  for keyword in keywords:
    name = re.sub(keyword, '', name)
  return name


def remove_year(name):
  name = re.sub('20[0-2][0-9]', '', name)
  name = re.sub('19[0-9][0-9]', '', name)
  return name


def remove_double_spaces(name):
  name = re.sub('  ', ' ', name)
  return name


def remove_trailing_symbols(name):
  symbols = ['-', ' ', '.']
  while len(name) > 0:
    c = name[-1]
    if c in symbols:
      name = name[0:-1]
    else:
      break
  return name


def remove_trailing_crap(name):
  name = re.sub(' -.*$', '', name)
  name = re.sub(' {2,}.*', '', name)
  return name


def fix_the_at_the_end(name):
  _name = re.sub(', the', '', name)
  if _name != name:
    name = ' '.join(['the',_name])
  _name = re.sub(' ,the', '', name)
  if _name != name:
    name = ' '.join(['the',_name])
  return name


def fix_a_at_the_end(name):
  _name = re.sub(', a', '', name)
  if _name != name:
    name = ' '.join(['a',_name])
  _name = re.sub(' ,a', '', name)
  if _name != name:
    name = ' '.join(['a',_name])
  return name


def recapitalize(name):
  exclude_words = ['and',
                   'or',
                   'in',
                   'to',
                   'the',
                   'of',
                   ]
  name = name.split(' ')
  if len(name) == 1:
    name[0] = name[0].upper()
  else:
    name[0] = name[0][0].upper()+name[0][1:] # Always capitalize the first word.

  for i, word in enumerate(name):
    if word not in exclude_words:
      if len(word) == 1:
        name[i] = word.upper()
      else:
        name[i] = word[0].upper() + word[1:]
  name = ' '.join(name)
  return name


class TestParsers(unittest.TestCase):
  def test_remove_tags(self):
    i = '[tag1] (tag2) some random craps (tagtag)'
    c = '  some random craps '
    r = remove_tags(i)
    self.assertEqual(c, r)

  def test_remove_resolution(self):
    i = 'this is a file name with a resolution 1029x320'
    c = 'this is a file name with a resolution '
    r = remove_resolution(i)
    self.assertEqual(c, r)

  def test_fix_the_at_the_end(self):
    i = 'best movie ever, the'
    c = 'the best movie ever'
    r = fix_the_at_the_end(i)
    self.assertEqual(c, r)

  def test_fix_a_at_the_end(self):
    i = 'very cool movie, a'
    c = 'a very cool movie'
    r = fix_a_at_the_end(i)
    self.assertEqual(c, r)

  def test_recapitalize(self):
    i = 'a movie title'
    c = 'A Movie Title'
    r = recapitalize(i)
    self.assertEqual(c, r)

    i = 'the movie title'
    c = 'The Movie Title'
    r = recapitalize(i)
    self.assertEqual(c, r)

    i = 'a movie in title'
    c = 'A Movie in Title'
    r = recapitalize(i)
    self.assertEqual(c, r)



if __name__ == '__main__':
  unittest.main()
import unittest
from movie_title_parser import parsers
import os


def parse_movie_title(file_name):
	"""
	Will attempt to parse out the title of a movie given a file name that contains the movie title.
	Most useful for torrented movies that follow a particular naming scheme
	"""
	movie_name = os.path.basename(file_name)
	movie_name = parsers.remove_extension(file_name)
	movie_name = movie_name.lower()
	movie_name = parsers.fix_word_seperators(movie_name)
	movie_name = parsers.remove_tags(movie_name)
	movie_name = parsers.remove_resolution(movie_name)
	movie_name = parsers.remove_keywords(movie_name)
	movie_name = parsers.remove_year(movie_name)
	movie_name = parsers.remove_trailing_symbols(movie_name)
	movie_name = parsers.remove_trailing_crap(movie_name)
	movie_name = parsers.fix_the_at_the_end(movie_name)
	movie_name = parsers.fix_a_at_the_end(movie_name)
	movie_name = parsers.remove_double_spaces(movie_name)
	movie_name = movie_name.strip()
	movie_name = parsers.recapitalize(movie_name)
	return movie_name


class TestMovieTitle(unittest.TestCase):
	def setUp(self):
		global test_files
		self.test_titles = [('47 Ronin 2013 1080p.mp4', '47 Ronin'),
							('Inside Out 2015.1080p.BluRay.x264.YIFY.mp4', 'Inside Out'),
							('A.Beautiful.Mind.2001.1080p.BrRip.x264.YIFY.mp4', 'A Beautiful Mind'),
							('Interstellar 1080p.BluRay.x264.YIFY.mp4', 'INTERSTELLAR'),
							('Algorithm.2014.1080p.Bluray.10-bit.x265.AC3.2.0.[UTR-HD].(DE8FC4F4).mkv', 'ALGORITHM'),
							('Iron Man 1 2008.1080p.BluRay.x264..mp4', 'Iron Man 1'),
							('Alien.Covenant.2017.1080p.WEB-DL.H264.AC3-EVO[EtHD].mkv', 'Alien Covenant'),
							('Iron Man 2 2010.1080p.BrRip.x264.YIFY.mp4', 'Iron Man 2'),
							('Amazing Spider-Man 2 ,The [2014] 720p.mp4', 'The Amazing Spider-man 2'),
							('Iron Man 3 2013.1080p.BluRay.x264.YIFY.mp4', 'Iron Man 3'),
							('American.Beauty.1999.1080p.BrRip.x264.mp4', 'American Beauty'),
							('Jack the Giant Slayer (720p).mp4', 'Jack the Giant Slayer'),
							('Ant-Man 2015 1080p BluRay x264 DTS-JYK.mkv', 'ANT-MAN'),
							('John.Wick.Chapter.2.2017.1080p.WEB-DL.DD5.1.H264-FGT.mkv', 'John Wick Chapter 2'),
							('Arrival.2016.1080p.WEB-DL.H264.AC3-EVO.mkv', 'ARRIVAL'),
							('Jurassic Park 1993.720p.BluRay.X264-AMIABLE.mkv', 'Jurassic Park'),
							('Assassins Creed.mkv', 'Assassins Creed'),
							('Jurassic Park III 2001 3Li BluRay.mkv', 'Jurassic Park Iii'),
							('Baby.Driver.2017.1080p.BluRay.x264-[YTS.AG].mp4', 'Baby Driver'),
							('Jurassic Park The Lost World 720p [H264-mp4].mp4', 'Jurassic Park the Lost World'),
							('Ballerina.2016.1080p.BluRay.REMUX.AVC.DTS-HD.MA.5.1-EPSiLON.mkv', 'BALLERINA'),
							('Jurassic World 2015.mp4', 'Jurassic World'),
							('Batman.and.Harley.Quinn.2017.1080p.BluRay.REMUX.AVC.DTS-HD.MA.5.1-EPSiLON.mkv', 'Batman and Harley Quinn'),
							('Kick Ass 2 2013.mp4', 'Kick Ass 2'),
							('Baywatch.2017.UNRATED.1080p.BluRay.x264.Atmos.TrueHD.7.1-HDC.mkv', 'BAYWATCH'),
							('Kingsman The Secret Service 2014.1080p.x264.mp4', 'Kingsman the Secret Service'),
							('Bokeh.2017.1080p.WEB-DL.DD5.1.H264-FGT.mkv', 'BOKEH'),
							('kumiko the treasure hunter.mp4', 'Kumiko the Treasure Hunter'),
							('Bourne Identity ,The 2002.1080p.BrRip.x264.mp4', 'The Bourne Identity'),
							('Life.mkv', 'LIFE'),
							('Bourne, Jason 2016.1080p.BluRay.x264.mkv', 'Bourne, Jason'),
							('Looper 2012 1080p.x264.mp4', 'LOOPER'),
							('Bourne Legacy ,The (2012) (1080p x265 DTS).mkv', 'The Bourne Legacy'),
							('Mad Max Fury Road 2015.1080p.x264..mp4', 'Mad Max Fury Road'),
							('Bourne Supremacy ,The 2004 HDDVD.1080.mp4', 'The Bourne Supremacy'),
							('Martian ,The 2015 [BDRip-720p].mkv', 'The Martian'),
							('Bourne Ultimatum, The 2007.1080p.BrRip.x264.YIFY.mp4', 'The Bourne Ultimatum'),
							('MARVEL Captain America The First Avenger BluRay.mp4', 'Captain America the First Avenger'),
							('Braven', 'BRAVEN'),
							('MARVEL Captain America The Winter Soldier 2014.1080p.BluRay.x264.YIFY.mp4', 'Captain America the Winter Soldier'),
							('Bridge to Terabithia (720p).mp4', 'Bridge to Terabithia'),
							('Million Ways to Die in the West, A.mp4', 'A Million Ways to Die in the West'),
							('Bright.2017.HDRip.XViD.AC3-ETRG.avi', 'BRIGHT'),
							('Noah 2014.720p.BluRay.x264.YIFY.mp4', 'NOAH'),
							('Cashback (720p).mkv', 'CASHBACK'),
							('Now You See Me (1080p).mkv', 'Now You See Me'),
							('Chips 2017 BDrip.mkv', 'CHIPS'),
							('Olympus Has Fallen (1080p).mp4', 'Olympus Has Fallen'),
							('Collide.2016.1080p.BluRay.H264.AAC-RARBG.mp4', 'COLLIDE'),
							('Pain and Gain (1080p).mkv', 'Pain and Gain'),
							('Dead Man Down (1080p).mp4', 'Dead Man Down'),
							('Pirates.Of.The.Caribbean.Dead.Men.Tell.No.Tales.2017.1080p.BluRay.x264-[YTS.AG].mp4', 'Pirates of the Caribbean Dead Men Tell No Tales'),
							('Dracula Untold (720p).mp4', 'Dracula Untold'),
							('pixels.mp4', 'PIXELS'),
							('Dragonheart.3.The.Sorcerers.Curse.2015.720p.BluRay.x264.YIFY.mp4', 'Dragonheart 3 the Sorcerers Curse'),
							('Planet Hulk.mp4', 'Planet Hulk'),
							('Edge of Tomorrow 2014.1080p.BluRay.x264.YIFY.mp4', 'Edge of Tomorrow'),
							('Rain Man (720p).mp4', 'Rain Man'),
							('Enders Game 2013.1080p.BluRay.DTS.x264.mkv', 'Enders Game'),
							('Shin.Godzilla.2016.1080p.BluRay.x264-[YTS.AG].mp4', 'Shin Godzilla'),
							('Erased (1080p).mp4', 'ERASED'),
							('Side Effects (720p).mp4', 'Side Effects'),
							('Eraser 1996 DivX ENG.avi', 'ERASER'),
							('Silence 2016 1080p WEB-DL x264 AC3-JYK.mkv', 'SILENCE'),
							('Eternal Sunshine of the Spotless Mind-2004(1080p).mp4', 'Eternal Sunshine of the Spotless Mind'),
							('Sleepless.2016.1080p.BRRip.x264.AAC-ETRG.mp4', 'SLEEPLESS'),
							('Ex Machina 2015.1080p.BluRay.DTS.x264.mkv', 'Ex Machina'),
							('Sleight.2016.1080p.BluRay.x264-DRONES.mkv', 'SLEIGHT'),
							('Expendables 1, The 2010.1080p.BrRip.x264.YIFY.mp4', 'The Expendables 1'),
							('Split.2016.1080p.BRRip.x264.AAC-ETRG.mp4', 'SPLIT'),
							('Expendables 3, The 2014 EXTENDED 1080p.x264.mkv', 'The Expendables 3'),
							('Suicide Squad.mp4', 'Suicide Squad'),
							('Fast and Furious 6 (1080p).mkv', 'Fast and Furious 6'),
							('Superman Cartoon (1080p).mp4', 'Superman Cartoon'),
							('Ghost.Rider 2.Spirit.Of.Vengeance.2011.720p.BluRay.x264.YIFY.mp4', 'Ghost Rider 2 Spirit of Vengeance'),
							('The Art of Getting By-2011(720p).mp4', 'The Art of Getting By'),
							('Ghost Rider 720p BRRip.mkv', 'Ghost Rider'),
							('The.BFG.2016.1080p.BluRay.x264-SPARKS.mkv', 'The Bfg'),
							('Ghost.World.2001.1080p.BluRay.x264.YIFY.mp4', 'Ghost World'),
							('The.Boss.Baby.2017.1080p.WEB-DL.6CH.ShAaNiG.mkv', 'The Boss Baby'),
							('Ghost Writer, The (720p) BlueRay.DTS.2xRus.Eng.mkv', 'The Ghost Writer'),
							('The.Dark.Tower.2017.1080p.BluRay.x264.mp4', 'The Dark Tower'),
							('Girl Fever (360p).mp4', 'Girl Fever'),
							('The Death of Superman', 'The Death of Superman'),
							('Good.Will.Hunting.1997.720p.BrRip.x264.YIFY.mp4', 'Good Will Hunting'),
							('The.Exception.2017.HDRip.XviD.AC3-CAT-Drama.avi', 'The Exception'),
							('Guardians.of.the.Galaxy.Vol.2.2017.1080p.BluRay.x264-SPARKS.mkv', 'Guardians of the Galaxy Vol 2'),
							('The Girl with All the Gifts.2016.Ds_Es.HDTV.RT4].mkv', 'The Girl With All the Gifts'),
							('guarians_of_the_galaxy_1080p.mp4', 'Guarians of the Galaxy'),
							('The Great Wall.mp4', 'The Great Wall'),
							('Hansel and Gretel Witch Hunters 2013.DVDRip.X264.AC3.mkv', 'Hansel and Gretel Witch Hunters'),
							('The.Hitmans.Bodyguard.2017.1080p.WEB-DL.DD5.1.x264-HB.mkv', 'The Hitmans Bodyguard'),
							('Harry Potter and the Chamber of Secrets (2002) (1080p x265 DTS).mkv', 'Harry Potter and the Chamber of Secrets'),
							('The Imposter 2012 1080p Blu-ray Remux AVC DTS-HD MA 5.1 - KRaLiMaRKo.mkv', 'The Imposter'),
							('Harry Potter And The Deathly Hallows Part 1 2010.1080p.Bluray.x264.mp4', 'Harry Potter and the Deathly Hallows Part 1'),
							('The Internship (1080p).mkv', 'The Internship'),
							('Harry Potter And The Deathly Hallows Part 2 2011.1080p.Bluray.x264.mp4', 'Harry Potter and the Deathly Hallows Part 2'),
							('The Jungle Book 1967.m4v', 'The Jungle Book'),
							('Harry Potter and the Goblet of Fire.BDrip.mkv', 'Harry Potter and the Goblet of Fire Bdrip'),
							('The.Jungle.Book.2016.1080p.BRRip.x264.AAC-ETRG.mp4', 'The Jungle Book'),
							('Harry Potter and the Half Blood Prince 2009 1080p.mp4', 'Harry Potter and the Half Blood Prince'),
							('The Last Witch Hunter - 2015.m4v', 'The Last Witch Hunter'),
							('Harry Potter and the Order of the Phoenix 2007.1080p.BRRip.x264.mp4', 'Harry Potter and the Order of the Phoenix'),
							('The Lost City Of Z 2016 BluRay.mp4', 'The Lost City of Z'),
							('Harry Potter And The Prisoner Of Azkaban.mp4', 'Harry Potter and the Prisoner of Azkaban'),
							('The Perks of Being a WallFlower-2012(1080p).mp4', 'The Perks of Being A Wallflower'),
							('Hellboy - Directors Cut 2004 Eng 1080p.mp4', 'HELLBOY'),
							('the_prestige.mp4', 'The Prestige'),
							('Hotel Transylvania 1 2012.BDRip.avi', 'Hotel Transylvania 1'),
							('The Shadow Effect 2017.HDRip.XviD.AC3CAT-Action, Thriller.avi', 'The Shadow Effect'),
							('Hotel Transylvania 2 2015.720p.WEBRip.x264..mp4', 'Hotel Transylvania 2'),
							('Ice.age.collision.course.2016.1080p.bluray.x264-NBY (1).mkv', 'Ice Age Collision Course'),
							('xXx.Return.of.Xander.Cage.2017.BDRip.1080p.60fps.GTP.mkv', 'Xxx Return of Xander Cage'),
							('Inception (1080p) [Russian, Ukrainian, Eng, Audio].mkv', 'INCEPTION')]
		test_files = self.test_titles


	def test_parse_movie_title(self):
		result = ''
		for filename, title in self.test_titles:
			result = parse_movie_title(filename)
			self.assertEqual(title, result)


if __name__ == '__main__':
	unittest.main()
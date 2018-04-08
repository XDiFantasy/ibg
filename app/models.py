from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey ,FLOAT, Text,Date
from sqlalchemy.orm import relationship
"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
class Strategy(Model):
    __tablename__ = "strategy"

    id = Column(Integer, primary_key=True)
    intro = Column(Text(512))
    sg_id = Column(Integer, ForeignKey('attr_ch.id'))
    pg_id = Column(Integer, ForeignKey('attr_ch.id'))
    sf_id = Column(Integer, ForeignKey('attr_ch.id'))
    pf_id = Column(Integer, ForeignKey('attr_ch.id'))
    c_id = Column(Integer, ForeignKey('attr_ch.id'))
    v_sg_id = Column(Integer, ForeignKey('attr_ch.id'))
    v_pg_id = Column(Integer, ForeignKey('attr_ch.id'))
    v_sf_id = Column(Integer, ForeignKey('attr_ch.id'))
    v_pf_id = Column(Integer, ForeignKey('attr_ch.id'))
    v_c_id = Column(Integer, ForeignKey('attr_ch.id'))

    sg = relationship('AttrCh',foreign_keys=sg_id)
    sf = relationship('AttrCh',foreign_keys=sf_id)
    pg = relationship('AttrCh',foreign_keys=pg_id)
    pf = relationship('AttrCh',foreign_keys=pf_id)
    c = relationship('AttrCh',foreign_keys=c_id)
    v_sg = relationship('AttrCh',foreign_keys=v_sg_id)
    v_pg = relationship('AttrCh',foreign_keys=v_pg_id)
    v_sf = relationship('AttrCh',foreign_keys=v_sf_id)
    v_pf = relationship('AttrCh',foreign_keys=v_pf_id)
    v_c = relationship('AttrCh',foreign_keys=v_c_id)


    def __repr__(self):
        return "<Strategy %r>" % self.id


class AttrCh(Model):
    __tablename__ = 'attr_ch'
    id = Column(Integer, primary_key=True)

    comment = Column(String(50))
    order = Column(String(200),default='fg_pct - three_pt_pct - fta_pct - oreb_pct - dreb_pct - ast_pct - tov_pct - stl_pct - blk_pct - pf_pct')
    fg_pct = Column(FLOAT,default=0)
    three_pt_pct = Column(FLOAT,default=0)
    fta_pct = Column(FLOAT,default=0)
    oreb_pct = Column(FLOAT,default=0)
    dreb_pct = Column(FLOAT,default=0)
    ast_pct = Column(FLOAT,default=0)
    tov_pct = Column(FLOAT,default=0)
    stl_pct = Column(FLOAT,default=0)
    blk_pct = Column(FLOAT,default=0)
    pf_pct = Column(FLOAT,default=0)

    def __repr__(self):
        return '<AttrCh %r : %r>' % (self.id, self.comment)


class Equip(Model):
    __tablename__ = 'equip'
    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    attr_ch_id = Column(Integer, ForeignKey('attr_ch.id'))

    attr_ch = relationship('AttrCh')
    

    def __repr__(self):
        return "<Equip %r, %r, %r>" % (self.id, self.name, self.attr_ch_id)   
class TeamInfo(Model):
    __tablename__ = 'team_info'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    city = Column(String(45))
    intro = Column(String(255))

    def __init__(self, name, city, intro):
        self.name, self.city, self.intro = (
            name, city, intro)

    def __repr__(self):
        return "<TeamInfo %r>" % self.id
class PlayerBase(Model):
    __tablename__ = 'player_base'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    birthday = Column(Date)
    country = Column(String(45))
    height = Column(FLOAT)
    weight = Column(FLOAT)
    armspan = Column(FLOAT)
    reach_height = Column(FLOAT)
    draft = Column(String(255))

    # season_data_id = Column(Integer, ForeignKey('season_data.id'))
    team_id = Column(Integer, ForeignKey("team_info.id"))
    cloth_num = Column(Integer)
    pos1 = Column(String(2))
    pos2 = Column(String(2))
    price = Column(Integer)
    score = Column(Integer)

    team = relationship("TeamInfo", backref='playerbase')

    def __init__(self, name, birthday, country, height, wieght, armspan,
                 reach_height, draft, team_id, cloth_num, pos1, pos2, price, score):
        (self.name, self.birthday, self.country, self.height, self.wieght, self.armspan,
         self.reach_height, self.draft, self.team_id,
         self.cloth_num, self.pos1, self.pos2, self.price, self.score) = (name, birthday, country,
                                                                          height, wieght, armspan, reach_height, draft,
                                                                          team_id, cloth_num, pos1, pos2, price, score)

    def __repr__(self):
        return "<PlayerBase %r : %r>" % (self.id,self.name)
class Theme(Model):
    __tablename__ = 'theme'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String(255), nullable=True)
    detail = Column(Text(512), nullable=True)
    price = Column(Integer, nullable=True)
    player_one_id = Column(Integer, ForeignKey('player_base.id'), nullable=False)
    player_two_id = Column(Integer, ForeignKey('player_base.id'), nullable=False)
    player_three_id = Column(Integer, ForeignKey('player_base.id'), nullable=False)

    player_one = relationship('PlayerBase',foreign_keys=player_one_id)
    player_two = relationship('PlayerBase',foreign_keys=player_two_id)
    player_three = relationship('PlayerBase',foreign_keys=player_three_id)



    def __repr__(self):
        return '<Theme %r>' % self.id


class FundType(Model):
    __tablename__ = 'fund_type'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    price = Column(Integer, nullable=True, default=0)
    rate = Column(FLOAT, nullable=True, default=1)


    def __repr__(self):
        return '<FundType %r>' % self.id

